"""
🌟 BASH MAGIC 🌟
Intelligent bash parameter compilation system with clean architecture.

This module provides:
- Parameter detection and type inference
- Environment and ScriptThing variable integration  
- Safe compilation with shell injection protection
- Beautiful argparse generation
"""

import re
import shlex
import argparse
import sys
import os
import threading
from typing import Dict, List, Set, Optional, Union, Any, NamedTuple
from dataclasses import dataclass, field
from pathlib import Path

from .parameter_parser import UnifiedParameterParser, ParameterInfo
from ..utils import store
from ..config.config import get_variable_preference, get_single_arg_convenience
from .analyzers.context import AnalysisContext





# Thread-safe lazy-loaded regex patterns for better startup performance
class RegexPatterns:
    """Thread-safe lazy-compiled regex patterns for better performance."""
    _positional_refs = None
    _variable_refs = None
    _variable_definitions = None
    _usage_patterns = None
    _lock = threading.RLock()  # Reentrant lock for nested calls
    
    @classmethod
    def get_positional_refs(cls):
        if cls._positional_refs is None:
            with cls._lock:
                # Double-check locking pattern
                if cls._positional_refs is None:
                    cls._positional_refs = re.compile(r'\$\{?([0-9]+)\}?')
        return cls._positional_refs
    
    @classmethod
    def get_variable_refs(cls):
        if cls._variable_refs is None:
            with cls._lock:
                # Double-check locking pattern
                if cls._variable_refs is None:
                    # Combined pattern for all variable reference types
                    cls._variable_refs = re.compile(r'''
                        \$\{?([a-zA-Z_][a-zA-Z0-9_]*)\}?|           # Basic $var or ${var}
                        \$\{([a-zA-Z_][a-zA-Z0-9_]*)\[[^\]]*\]\}|   # Array access ${var[index]}
                        \$\{([a-zA-Z_][a-zA-Z0-9_]*)[:#%/][^}]*\}|  # Parameter expansion ${var:offset}, ${var#pattern}, etc.
                        \$\{([a-zA-Z_][a-zA-Z0-9_]*)\|\|[^}]*\}|    # Default value ${var||default}
                        \$\{([a-zA-Z_][a-zA-Z0-9_]*)\?\?[^}]*\}     # Error if unset ${var??error}
                    ''', re.VERBOSE)
        return cls._variable_refs
    
    @classmethod
    def get_variable_definitions(cls):
        if cls._variable_definitions is None:
            with cls._lock:
                # Double-check locking pattern
                if cls._variable_definitions is None:
                    cls._variable_definitions = [
                        # Basic assignments
                        re.compile(r'(?:^|[;\s])([a-zA-Z_][a-zA-Z0-9_]*)='),  # VAR=value (start of line or after ; or space)
                        re.compile(r'export\s+([a-zA-Z_][a-zA-Z0-9_]*)(?:=|$)'),  # export VAR or export VAR=value
                        re.compile(r'local\s+([a-zA-Z_][a-zA-Z0-9_]*)(?:=|$)'),  # local VAR or local VAR=value
                        re.compile(r'declare\s+(?:-[a-zA-Z]+\s+)?([a-zA-Z_][a-zA-Z0-9_]*)(?:=|$)'),  # declare VAR
                        re.compile(r'readonly\s+([a-zA-Z_][a-zA-Z0-9_]*)(?:=|$)'),  # readonly VAR
                        
                        # Command substitution assignments
                        re.compile(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*\$\('),  # VAR=$(command)
                        re.compile(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*`'),  # VAR=`command`
                        
                        # Arithmetic expansion assignments
                        re.compile(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*\$\(\('),  # VAR=$((expression))
                        re.compile(r'\(\(\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*[=+\-*/]'),  # ((VAR=expr)) or ((VAR+=1))
                        
                        # Array assignments
                        re.compile(r'([a-zA-Z_][a-zA-Z0-9_]*)\[\d*\]\s*='),  # VAR[0]=value or VAR[]=value
                        re.compile(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*\('),  # VAR=(array elements)
                        
                        # Input/loops
                        re.compile(r'read\s+(?:-[a-zA-Z]+\s+)?([a-zA-Z_][a-zA-Z0-9_]*)'),  # read VAR
                        re.compile(r'for\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+in'),  # for VAR in
                        re.compile(r'while\s+read\s+([a-zA-Z_][a-zA-Z0-9_]*)'),  # while read VAR
                        re.compile(r'select\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+in'),  # select VAR in
                        
                        # Functions
                        re.compile(r'function\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\('),  # function definitions
                        re.compile(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*\(\s*\)\s*\{'),  # function name() { definitions
                        
                        # Parameter expansion with assignment
                        re.compile(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*:\s*='),  # VAR:=default (parameter expansion)
                    ]
        return cls._variable_definitions
    
    @classmethod
    def get_usage_patterns(cls):
        if cls._usage_patterns is None:
            with cls._lock:
                # Double-check locking pattern
                if cls._usage_patterns is None:
                    cls._usage_patterns = [
                        re.compile(r'#\s*USAGE:\s*(.+)', re.IGNORECASE),  # Handles all case variations
                    ]
        return cls._usage_patterns


# Constants for better maintainability
class Constants:
    """System constants and configuration."""
    BASH_BUILTIN_VARS = {
        # Core bash variables
        'BASH', 'BASH_VERSION', 'BASH_VERSINFO', 'BASHPID', 'BASHOPTS', 'SHELLOPTS',
        'IFS', 'PS1', 'PS2', 'PS3', 'PS4', 'PROMPT_COMMAND',
        'HISTFILE', 'HISTSIZE', 'HISTCONTROL', 'HISTIGNORE', 'HISTTIMEFORMAT',
        'FUNCNAME', 'BASH_LINENO', 'BASH_SOURCE', 'BASH_SUBSHELL',
        'GROUPS', 'PIPESTATUS', 'BASH_REMATCH', 'BASH_ARGV', 'BASH_ARGC',
        
        # Additional common variables
        'OLDPWD', 'PWD', 'RANDOM', 'SECONDS', 'LINENO', 'EPOCHSECONDS', 'EPOCHREALTIME',
        'BASH_COMMAND', 'BASH_EXECUTION_STRING', 'BASH_LOADABLES_PATH',
        'COMP_CWORD', 'COMP_LINE', 'COMP_POINT', 'COMP_TYPE', 'COMP_KEY',
        'COMP_WORDBREAKS', 'COMP_WORDS', 'COMPREPLY',
        
        # Environment-related
        'COLUMNS', 'LINES', 'TERM', 'TERMINFO', 'TERMCAP', 'DISPLAY',
        'EDITOR', 'VISUAL', 'PAGER', 'BROWSER', 'SHELL', 'SHLVL',
        
        # Process-related  
        'PPID', 'UID', 'EUID', 'GID', 'EGID', 'HOSTNAME', 'HOSTTYPE', 'MACHTYPE', 'OSTYPE'
    }
    
    BASH_SPECIAL_VARS = {'#', '?', '$', '!', '0', '*', '@', '-', '_'}
    
    TYPE_PATTERNS = {
        'bool': ['verbose', 'debug', 'quiet', 'force', 'dry_run', 'enable', 'disable'],
        'int': ['count', 'num', 'size', 'limit', 'max', 'min', 'port', 'timeout'],
        'path': ['file', 'path', 'dir', 'directory', 'output', 'input']
    }
    
    # Resource limits to prevent DoS
    MAX_SCRIPT_SIZE = 1_000_000  # 1MB
    MAX_PARAMETERS = 1000  # Maximum number of parameters
    MAX_LINE_LENGTH = 10_000  # Maximum line length
    MAX_VARIABLE_NAME_LENGTH = 255  # Maximum variable name length


class VariableResolution(NamedTuple):
    """Clean data structure for variable resolution results."""
    primary: Dict[str, str]
    secondary: Dict[str, str] 
    conflicts: Dict[str, Dict[str, str]]


def add_global_options(parser: argparse.ArgumentParser) -> None:
    """Add global ScriptThing options to any parser."""
    global_group = parser.add_argument_group('ScriptThing Global Options')
    global_group.add_argument(
        '--st-prefer',
        choices=['env', 'scriptthing'],
        help='Override variable preference for this execution (env: prefer environment variables, scriptthing: prefer scriptthing variables)'
    )


@dataclass
class BashParameter:
    """A bash parameter with comprehensive metadata."""
    name: str
    type: str = 'positional'  # 'positional' or 'option'
    position: Optional[int] = None
    flag: Optional[str] = None
    description: str = ""
    required: bool = True
    default: Optional[str] = None
    var_type: str = 'str'  # 'str', 'int', 'float', 'bool', 'path'
    choices: Optional[List[str]] = None
    min_value: Optional[Union[int, float]] = None
    max_value: Optional[Union[int, float]] = None
    
    def __post_init__(self):
        """Auto-generate missing fields."""
        if self.type == 'positional' and not self.description:
            self.description = f"{self.name} (positional argument {self.position})"
        elif self.type == 'option' and not self.description:
            self.description = f"Value for ${self.name}"
        
        if self.type == 'option' and not self.flag:
            self.flag = f"--{self.name.lower().replace('_', '-')}"


class ScriptAnalyzer:
    """Analyzes bash scripts to extract parameter information."""
    
    def __init__(self, content: str):
        if not isinstance(content, str):
            raise TypeError(f"Script content must be a string, got {type(content)}")
        if len(content) > Constants.MAX_SCRIPT_SIZE:
            raise ValueError(f"Script too large ({len(content)} chars). Maximum size is {Constants.MAX_SCRIPT_SIZE} chars.")
        
        self.content = content
        self.lines = content.split('\n')
        
        # Check for excessively long lines that could cause regex issues
        for line_num, line in enumerate(self.lines, 1):
            if len(line) > Constants.MAX_LINE_LENGTH:
                raise ValueError(f"Line {line_num} is too long ({len(line)} chars). Maximum line length is {Constants.MAX_LINE_LENGTH} chars.")
    
    def find_positional_references(self) -> Set[int]:
        """Find all positional parameter references ($1, $2, ${10}, etc.)."""
        try:
            matches = RegexPatterns.get_positional_refs().findall(self.content)
            return set(int(match) for match in matches)
        except re.error as e:
            raise ValueError(f"Failed to parse positional references: {e}")
        except ValueError as e:
            if "invalid literal for int()" in str(e):
                raise ValueError(f"Invalid positional parameter number in script: {e}")
            raise
    
    def find_variable_references(self) -> Set[str]:
        """Find all variable references ($var, ${var}, arrays, parameter expansion)."""
        try:
            # The regex has multiple capture groups, so we get tuples
            matches = RegexPatterns.get_variable_refs().findall(self.content)
            var_refs = set()
            
            for match in matches:
                # match is a tuple of capture groups, find the non-empty one
                if isinstance(match, tuple):
                    for group in match:
                        if group:  # Non-empty group
                            var_refs.add(group)
                            break
                else:
                    var_refs.add(match)
            
            # Validate variable name lengths
            for var in var_refs:
                if len(var) > Constants.MAX_VARIABLE_NAME_LENGTH:
                    raise ValueError(f"Variable name '{var}' is too long ({len(var)} chars). Maximum length is {Constants.MAX_VARIABLE_NAME_LENGTH} chars.")
            
            return var_refs
        except re.error as e:
            raise ValueError(f"Failed to parse variable references: {e}")
    
    def find_defined_variables(self) -> Set[str]:
        """Find variables that are defined in the script."""
        defined_vars = set()
        
        try:
            for line_num, line in enumerate(self.lines, 1):
                line = line.strip()
                for pattern in RegexPatterns.get_variable_definitions():
                    try:
                        defined_vars.update(pattern.findall(line))
                    except re.error as e:
                        raise ValueError(f"Regex error on line {line_num}: {e}")
        except re.error as e:
            raise ValueError(f"Failed to parse variable definitions: {e}")
        
        return defined_vars
    
    def find_undefined_variables(self) -> Set[str]:
        """Find variables that are referenced but not defined in the script."""
        var_refs = self.find_variable_references()
        defined_vars = self.find_defined_variables()
        
        # Exclude bash built-ins and special variables
        excluded = Constants.BASH_BUILTIN_VARS | Constants.BASH_SPECIAL_VARS
        
        return var_refs - defined_vars - excluded
    
    def find_usage_comment(self) -> Optional[str]:
        """Find USAGE comment with flexible formatting."""
        for line in self.lines:
            for pattern in RegexPatterns.get_usage_patterns():
                match = pattern.search(line.strip())
                if match:
                    return match.group(1).strip()
        return None


class VariableResolver:
    """Resolves conflicts between environment and scriptthing variables."""
    
    def __init__(self, preference_override: Optional[str] = None):
        self.preference = preference_override or get_variable_preference()
    
    def get_environment_variables(self, var_refs: Set[str]) -> Dict[str, str]:
        """Get environment variables that are referenced in the script."""
        return {var: os.environ[var] for var in var_refs if var in os.environ}
    
    def get_scriptthing_variables(self, var_refs: Set[str]) -> Dict[str, str]:
        """Get scriptthing variables that are referenced in the script."""
        try:
            # The store module should handle its own thread safety
            # We just need to ensure we don't modify shared state here
            all_vars = store._get_all()
            return {
                var: str(all_vars[var]['value']) 
                for var in var_refs 
                if var in all_vars
            }
        except Exception as e:
            # Log the error but continue - scriptthing variables are optional
            import logging
            logging.getLogger(__name__).warning(
                f"Failed to retrieve scriptthing variables: {e}. "
                f"Continuing without scriptthing variable defaults."
            )
            return {}
    
    def resolve_conflicts(self, env_vars: Dict[str, str], scriptthing_vars: Dict[str, str]) -> VariableResolution:
        """Resolve conflicts between environment and scriptthing variables."""
        primary = {}
        secondary = {}
        conflicts = {}
        
        # Process env vars first
        for var, env_value in env_vars.items():
            scriptthing_value = scriptthing_vars.get(var)
            
            if scriptthing_value is not None:
                # Conflict exists
                conflicts[var] = {
                    'env': env_value,
                    'scriptthing': scriptthing_value,
                    'preference': self.preference
                }
                
                if self.preference == 'env':
                    primary[var] = env_value
                    secondary[var] = scriptthing_value
                else:
                    primary[var] = scriptthing_value
                    secondary[var] = env_value
            else:
                primary[var] = env_value
        
        # Process remaining scriptthing vars (no conflicts)
        for var, scriptthing_value in scriptthing_vars.items():
            if var not in env_vars:
                primary[var] = scriptthing_value
        
        return VariableResolution(primary, secondary, conflicts)


class TypeInferrer:
    """Infers parameter types and defaults from names and values."""
    
    @staticmethod
    def infer_type_from_name(name: str) -> str:
        """Infer parameter type from name patterns."""
        name_lower = name.lower()
        
        for var_type, keywords in Constants.TYPE_PATTERNS.items():
            if any(keyword in name_lower for keyword in keywords):
                return var_type
        
        return 'str'
    
    @staticmethod
    def infer_type_from_value(value: str) -> str:
        """Infer parameter type from actual value with robust validation."""
        if not value:  # Empty string
            return 'str'
        
        # Integer check - must be all digits or negative digits
        if value.isdigit() or (value.startswith('-') and len(value) > 1 and value[1:].isdigit()):
            return 'int'
        
        # Float check - must have exactly one dot and valid numeric parts
        if '.' in value and value.count('.') == 1:
            parts = value.split('.')
            if len(parts) == 2:
                left, right = parts
                # Left part: empty, digits, or negative digits
                left_valid = (not left or left.isdigit() or 
                             (left.startswith('-') and len(left) > 1 and left[1:].isdigit()))
                # Right part: must be digits
                right_valid = right.isdigit()
                
                if left_valid and right_valid:
                    return 'float'
        
        # Boolean check - common boolean representations
        if value.lower() in ['true', 'false', 'yes', 'no', '1', '0', 'on', 'off']:
            return 'bool'
        
        return 'str'
    
    @staticmethod
    def infer_default(name: str, var_type: str) -> Optional[str]:
        """Infer sensible defaults for parameters."""
        if var_type == 'bool':
            name_lower = name.lower()
            if any(keyword in name_lower for keyword in ['verbose', 'debug', 'force']):
                return 'false'
        return None
    
    @staticmethod
    def infer_required(name: str) -> bool:
        """Infer if parameter should be required."""
        name_lower = name.lower()
        optional_keywords = ['verbose', 'debug', 'quiet', 'dry_run']
        return not any(keyword in name_lower for keyword in optional_keywords)


class ParameterBuilder:
    """Builds BashParameter objects with intelligent defaults and metadata."""
    
    def __init__(self, metadata_overrides: Dict[str, Dict[str, Any]], variable_resolution: VariableResolution):
        self.metadata_overrides = metadata_overrides
        self.variable_resolution = variable_resolution
        self.type_inferrer = TypeInferrer()
    
    def build_positional_parameters(self, positional_refs: Set[int]) -> List[BashParameter]:
        """Build positional parameters."""
        return [
            BashParameter(
                name=f'ARG{pos}',
                type='positional',
                position=pos
            )
            for pos in sorted(positional_refs)
        ]
    
    def build_option_parameters(self, undefined_vars: Set[str]) -> List[BashParameter]:
        """Build option parameters from undefined variables."""
        parameters = []
        
        for var in sorted(undefined_vars):
            param = BashParameter(name=var, type='option')
            self._enhance_parameter(param)
            parameters.append(param)
        
        return parameters
    
    def _enhance_parameter(self, param: BashParameter) -> None:
        """Enhance parameter with type inference, defaults, and metadata."""
        # Start with intelligent defaults
        param.var_type = self.type_inferrer.infer_type_from_name(param.name)
        param.default = self.type_inferrer.infer_default(param.name, param.var_type)
        param.required = self.type_inferrer.infer_required(param.name)
        
        # Apply variable defaults if available
        if param.name in self.variable_resolution.primary:
            self._apply_variable_default(param)
        
        # Apply metadata overrides (highest priority)
        if param.name in self.metadata_overrides:
            self._apply_metadata_overrides(param)
    
    def _apply_variable_default(self, param: BashParameter) -> None:
        """Apply variable default and update parameter accordingly."""
        value = self.variable_resolution.primary[param.name]
        param.default = value
        param.required = False
        
        # Infer type from actual value
        inferred_type = self.type_inferrer.infer_type_from_value(value)
        if inferred_type != 'str':  # Override name-based inference if we have better info
            param.var_type = inferred_type
        
        # Update description with source information
        self._update_description_with_source(param)
    
    def _update_description_with_source(self, param: BashParameter) -> None:
        """Update parameter description with variable source information."""
        if param.name in self.variable_resolution.conflicts:
            param._conflict_info = self.variable_resolution.conflicts[param.name]
            conflict = param._conflict_info
            preference = conflict['preference']
            primary_source = 'environment' if preference == 'env' else 'scriptthing'
            secondary_source = 'scriptthing' if preference == 'env' else 'environment'
            
            if not param.description:
                param.description = f"Value for ${param.name} ({primary_source} default: {self.variable_resolution.primary[param.name]}, {secondary_source}: {self.variable_resolution.secondary[param.name]})"
            else:
                param.description += f" ({primary_source} default: {self.variable_resolution.primary[param.name]}, {secondary_source}: {self.variable_resolution.secondary[param.name]})"
        else:
            # Single source - determine from variable resolution data
            env_vars = {var: os.environ[var] for var in self.variable_resolution.primary.keys() if var in os.environ}
            source = 'environment' if param.name in env_vars else 'scriptthing'
            
            if not param.description:
                param.description = f"Value for ${param.name} ({source} default: {self.variable_resolution.primary[param.name]})"
            else:
                param.description += f" ({source} default: {self.variable_resolution.primary[param.name]})"
    
    def _apply_metadata_overrides(self, param: BashParameter) -> None:
        """Apply metadata overrides to parameter."""
        meta = self.metadata_overrides[param.name]
        
        # Only override if explicitly set (not None/default values)
        if meta.get('var_type') is not None:
            param.var_type = meta['var_type']
        if meta.get('description') is not None:
            param.description = meta['description']
        if meta.get('default') is not None:
            param.default = meta['default']
        if meta.get('required') is not None and meta.get('default') is None and param.default is None:
            # Only override required if no default is set anywhere (metadata or variables)
            param.required = meta['required']
        if meta.get('choices') is not None:
            param.choices = meta['choices']
        if meta.get('min_value') is not None:
            param.min_value = meta['min_value']
        if meta.get('max_value') is not None:
            param.max_value = meta['max_value']


@dataclass
class BashScript:
    """
    A bash script with intelligent parameter understanding.
    
    Thread-safe: Each instance maintains its own state without shared mutable data.
    The only shared resources are the compiled regex patterns, which are thread-safe.
    """
    path: Path
    content: str
    preference_override: Optional[str] = None
    parameters: List[BashParameter] = field(default_factory=list)
    usage_comment: Optional[str] = None
    has_parameters: bool = False
    
    def __post_init__(self):
        """Analyze the script and extract parameters."""
        self._analyze()
    
    def _analyze(self):
        """Analyze the script using clean, separated components."""
        analyzer = ScriptAnalyzer(self.content)
        resolver = VariableResolver(self.preference_override)
        
        # Extract basic parameter data
        positional_refs = analyzer.find_positional_references()
        variable_refs = analyzer.find_variable_references()
        undefined_vars = analyzer.find_undefined_variables()
        self.usage_comment = analyzer.find_usage_comment()
        
        # Resolve variable conflicts
        env_vars = resolver.get_environment_variables(variable_refs)
        scriptthing_vars = resolver.get_scriptthing_variables(variable_refs)
        variable_resolution = resolver.resolve_conflicts(env_vars, scriptthing_vars)
        
        # Parse metadata comments
        metadata_overrides = self._parse_metadata_comments()
        
        # Build parameters
        builder = ParameterBuilder(metadata_overrides, variable_resolution)
        
        if self.usage_comment:
            self.parameters = self._parse_usage_guided(positional_refs, undefined_vars, builder)
        else:
            positional_params = builder.build_positional_parameters(positional_refs)
            option_params = builder.build_option_parameters(undefined_vars)
            self.parameters = sorted(positional_params + option_params, key=lambda p: (p.type != 'positional', p.position or 0))
        
        # Validate parameter count to prevent resource exhaustion
        if len(self.parameters) > Constants.MAX_PARAMETERS:
            raise ValueError(f"Too many parameters ({len(self.parameters)}). Maximum allowed is {Constants.MAX_PARAMETERS}.")
        
        self.has_parameters = bool(self.parameters)
    
    def _parse_metadata_comments(self) -> Dict[str, Dict[str, Any]]:
        """Parse metadata comments using the unified parameter parser."""
        unified_parser = UnifiedParameterParser()
        result = unified_parser.parse(self.content)
        
        return {
            param.name: {
                'var_type': param.param_type.value,
                'description': param.description,
                'default': param.default,
                'required': param.required,
                'choices': param.choices,
                'min_value': param.min_value,
                'max_value': param.max_value
            }
            for param in result.parameters
        }
    
    def _parse_usage_guided(self, positional_refs: Set[int], undefined_vars: Set[str], builder: ParameterBuilder) -> List[BashParameter]:
        """Parse parameters guided by USAGE comment."""
        parameters = []
        tokens = self.usage_comment.split()[1:]  # Skip command name
        mentioned_vars = set()
        pos_index = 1
        
        for token in tokens:
            if token.startswith('--'):
                # Option parameter
                opt_name = token[2:]
                var_name = self._find_matching_var(opt_name, undefined_vars)
                if var_name:
                    param = BashParameter(name=var_name, type='option', flag=token)
                    builder._enhance_parameter(param)
                    parameters.append(param)
                    mentioned_vars.add(var_name)
            elif not token.startswith('-') and not token.startswith('['):
                # Positional parameter
                if pos_index in positional_refs:
                    parameters.append(BashParameter(
                        name=token.upper(),
                        type='positional',
                        position=pos_index,
                        description=f"{token} (positional argument {pos_index})"
                    ))
                    matching_var = self._find_matching_var(token, undefined_vars)
                    if matching_var:
                        mentioned_vars.add(matching_var)
                pos_index += 1
        
        # Add remaining positional args
        for pos in sorted(positional_refs):
            if not any(p.position == pos for p in parameters):
                parameters.append(BashParameter(
                    name=f'ARG{pos}',
                    type='positional',
                    position=pos
                ))
        
        # Add remaining undefined vars as options
        remaining_vars = undefined_vars - mentioned_vars
        option_params = builder.build_option_parameters(remaining_vars)
        parameters.extend(option_params)
        
        return sorted(parameters, key=lambda p: (p.type != 'positional', p.position or 0))
    
    def _find_matching_var(self, token: str, undefined_vars: Set[str]) -> Optional[str]:
        """Find matching variable with flexible name matching."""
        token_normalized = token.lower().replace('-', '').replace('_', '')
        
        for var in undefined_vars:
            var_normalized = var.lower().replace('-', '').replace('_', '')
            if var_normalized == token_normalized:
                return var
        
        return None
    
    def create_parser(self) -> Optional[argparse.ArgumentParser]:
        """Create an elegant argparse parser."""
        if not self.has_parameters:
            return None
        
        parser = argparse.ArgumentParser(
            prog=self.path.name,
            description=f"✨ {self.path.name} ✨"
        )
        
        add_global_options(parser)
        
        # Check for single argument convenience feature
        if self._should_enable_single_arg_convenience():
            self._add_single_arg_convenience(parser)
        else:
            self._add_positional_arguments(parser)
            self._add_option_arguments(parser)
        
        return parser
    
    def _should_enable_single_arg_convenience(self) -> bool:
        """Check if single argument convenience should be enabled."""
        # Check if the feature is enabled in config
        if not get_single_arg_convenience():
            return False
        
        # Only enable if there's exactly one parameter total
        if len(self.parameters) != 1:
            return False
        
        # Get the single parameter
        param = self.parameters[0]
        
        # Only enable for option parameters (variables) since positional args already work
        # The convenience is to allow both positional and option syntax for a single variable
        return param.type == 'option'
    
    def _add_single_arg_convenience(self, parser: argparse.ArgumentParser) -> None:
        """Add single argument with both positional and option syntax support."""
        param = self.parameters[0]
        
        # Create a custom argument parser that accepts both forms
        help_text = self._build_help_text(param)
        help_text += f"\n📝 Convenience: Can be provided as positional argument or {param.flag}"
        
        # Add as positional with special destination to distinguish it
        positional_dest = f"{param.name}_positional"
        parser.add_argument(
            positional_dest,
            nargs='?',  # Optional positional
            help=help_text,
            metavar=param.name.upper(),
            type=self._get_argparse_type(param.var_type),
            default=argparse.SUPPRESS  # Don't set default here, handle in validation
        )
        
        # Add the option form too with original destination
        option_kwargs = self._build_argument_kwargs(param, help_text)
        option_kwargs['default'] = argparse.SUPPRESS  # Don't set default here either
        option_kwargs['required'] = False  # Not required since positional can be used instead
        parser.add_argument(param.flag, **option_kwargs)
    
    def _process_single_arg_convenience(self, parsed) -> Dict[str, Any]:
        """Process parsed arguments for single argument convenience feature."""
        param = self.parameters[0]
        positional_dest = f"{param.name}_positional"
        option_name = param.name
        
        # Check what was provided
        positional_value = getattr(parsed, positional_dest, None)
        option_value = getattr(parsed, option_name, None)
        
        # Handle the SUPPRESS sentinel values
        if positional_value is argparse.SUPPRESS:
            positional_value = None
        if option_value is argparse.SUPPRESS:
            option_value = None
        
        # Validate that both forms weren't provided
        if positional_value is not None and option_value is not None:
            raise ValueError(f"Cannot provide both positional argument '{positional_value}' and option {param.flag} '{option_value}'. Use one or the other.")
        
        # Determine the final value
        final_value = positional_value if positional_value is not None else option_value
        
        # If no value provided, check for default or if required
        if final_value is None:
            if param.default is not None:
                final_value = param.default
            elif param.required:
                raise ValueError(f"Missing required parameter. Provide either a positional argument or {param.flag}.")
        
        # Return in the expected format
        result = {}
        if final_value is not None:
            result[param.name] = str(final_value) if param.var_type != 'bool' else final_value
        
        return result
    
    def _add_positional_arguments(self, parser: argparse.ArgumentParser) -> None:
        """Add positional arguments to parser."""
        for param in [p for p in self.parameters if p.type == 'positional']:
            parser.add_argument(
                param.name.lower(),
                help=param.description,
                metavar=param.name,
                type=self._get_argparse_type(param.var_type)
            )
    
    def _add_option_arguments(self, parser: argparse.ArgumentParser) -> None:
        """Add option arguments to parser."""
        for param in [p for p in self.parameters if p.type == 'option']:
            help_text = self._build_help_text(param)
            kwargs = self._build_argument_kwargs(param, help_text)
            parser.add_argument(param.flag, **kwargs)
    
    def _build_help_text(self, param: BashParameter) -> str:
        """Build comprehensive help text for parameter."""
        help_text = param.description
        
        # Add conflict warning if this parameter has conflicting sources
        if hasattr(param, '_conflict_info') and param._conflict_info:
            conflict = param._conflict_info
            preference = conflict['preference']
            env_val = conflict['env']
            st_val = conflict['scriptthing']
            
            help_text += f"\n⚠️  CONFLICT: Both environment ({env_val}) and scriptthing ({st_val}) variables exist."
            help_text += f"\n   Current setting will use: {conflict[preference]} (preference: {preference})"
            help_text += f"\n   Override with: --st-prefer env or --st-prefer scriptthing"
        
        if param.choices:
            help_text += f" | Choices: {', '.join(param.choices)}"
        
        if param.min_value is not None or param.max_value is not None:
            range_info = []
            if param.min_value is not None:
                range_info.append(f"min: {param.min_value}")
            if param.max_value is not None:
                range_info.append(f"max: {param.max_value}")
            help_text += f" | Range: {', '.join(range_info)}"
        
        return help_text
    
    def _build_argument_kwargs(self, param: BashParameter, help_text: str) -> Dict[str, Any]:
        """Build kwargs for argparse argument."""
        kwargs = {
            'dest': param.name,
            'help': help_text,
            'metavar': param.name.upper(),
        }
        
        if param.var_type == 'bool':
            kwargs['action'] = 'store_true' if param.default == 'false' else 'store_false'
            kwargs.pop('metavar')
            kwargs['required'] = False
        else:
            kwargs['type'] = self._get_argparse_type(param.var_type)
            kwargs['required'] = param.required
            if param.default is not None:
                kwargs['default'] = param.default
                kwargs['required'] = False
        
        if param.choices:
            kwargs['choices'] = param.choices
        
        return kwargs
    
    def _get_argparse_type(self, var_type: str):
        """Get argparse type function."""
        type_map = {
            'str': str,
            'int': int,
            'float': float,
            'path': Path,
            'bool': bool
        }
        return type_map.get(var_type, str)
    
    def parse_args(self, args: List[str], _recursion_depth: int = 0) -> Optional[Dict[str, Any]]:
        """Parse arguments with grace and intelligence."""
        if _recursion_depth > 1:
            raise RuntimeError("Maximum recursion depth exceeded in preference override")
        
        parser = self.create_parser()
        if not parser:
            return None
        
        try:
            parsed = parser.parse_args(args)
            
            # Check for global preference overrides
            preference_override = getattr(parsed, 'st_prefer', None)
            
            # If preference override differs from current, re-analyze and re-parse
            if preference_override and preference_override != (self.preference_override or get_variable_preference()):
                new_script = BashScript(self.path, self.content, preference_override)
                return new_script.parse_args(args, _recursion_depth + 1)
            
            # Handle single argument convenience validation and conversion
            if self._should_enable_single_arg_convenience():
                return self._process_single_arg_convenience(parsed)
            else:
                # Convert parsed args to our format (normal case)
                result = {}
                for param in self.parameters:
                    key = param.name.lower() if param.type == 'positional' else param.name
                    value = getattr(parsed, key, param.default)
                    if value is not None:
                        result[key] = str(value) if param.var_type != 'bool' else value
                
                return result
            
        except SystemExit as e:
            if e.code == 0:  # Help was shown
                sys.exit(0)
            else:  # Error occurred
                print(f"\n💡 Tip: Use --help to see all available options!", file=sys.stderr)
                sys.exit(1)
    
    def compile_with_params(self, param_values: Dict[str, Any]) -> str:
        """Compile script with parameter substitution and validation."""
        if not self.has_parameters:
            return self.content
        
        # Validate required parameters are provided
        self._validate_required_parameters(param_values)
        
        # Build substitution map for single-pass replacement
        substitutions = {}
        
        # Add positional arguments
        for param in [p for p in self.parameters if p.type == 'positional']:
            if param.name.lower() in param_values:
                value = param_values[param.name.lower()]
                safe_value = self._get_safe_value(value)
                substitutions[f'${param.position}'] = safe_value
            elif param.required:
                raise ValueError(f"Required positional parameter '{param.name}' (${param.position}) not provided")
        
        # Add named variables with extended pattern support
        for param in [p for p in self.parameters if p.type == 'option']:
            if param.name in param_values:
                value = param_values[param.name]
                safe_value = self._get_safe_value(value)
                
                # Basic patterns
                substitutions[f'${param.name}'] = safe_value
                substitutions[f'${{{param.name}}}'] = safe_value
                
                # Array access patterns (treat as single value for now)
                substitutions[f'${{{param.name}[0]}}'] = safe_value
                substitutions[f'${{{param.name}[@]}}'] = safe_value
                substitutions[f'${{{param.name}[*]}}'] = safe_value
                
                # Parameter expansion patterns with defaults
                # ${var:-default} -> use var if set, otherwise default
                # ${var:=default} -> use var if set, otherwise set and use default
                # For our purposes, since we have the value, just substitute it
                param_expansion_pattern = re.compile(rf'\$\{{{param.name}[:#%/][^}}]*\}}')
                for match in param_expansion_pattern.findall(self.content):
                    substitutions[match] = safe_value
                    
            elif param.required:
                raise ValueError(f"Required parameter '--{param.name}' not provided")
        
        # Single-pass substitution
        return self._perform_substitutions(self.content, substitutions)
    
    def _validate_required_parameters(self, param_values: Dict[str, Any]) -> None:
        """Validate that all required parameters are provided."""
        missing_params = []
        
        for param in self.parameters:
            if param.required:
                if param.type == 'positional':
                    key = param.name.lower()
                    if key not in param_values or param_values[key] is None:
                        missing_params.append(f"${param.position} ({param.name})")
                else:  # option
                    if param.name not in param_values or param_values[param.name] is None:
                        missing_params.append(f"--{param.name}")
        
        if missing_params:
            param_list = ", ".join(missing_params)
            raise ValueError(f"Missing required parameters: {param_list}")
        
        # Validate parameter constraints (choices, ranges)
        self._validate_parameter_constraints(param_values)
    
    def _validate_parameter_constraints(self, param_values: Dict[str, Any]) -> None:
        """Validate parameter values against their constraints."""
        for param in self.parameters:
            key = param.name.lower() if param.type == 'positional' else param.name
            
            if key in param_values and param_values[key] is not None:
                value = param_values[key]
                
                # Validate choices
                if param.choices and str(value) not in param.choices:
                    raise ValueError(f"Parameter '{param.name}' must be one of: {', '.join(param.choices)}. Got: {value}")
                
                # Validate numeric ranges
                if param.var_type in ['int', 'float'] and (param.min_value is not None or param.max_value is not None):
                    try:
                        numeric_value = float(value) if param.var_type == 'float' else int(value)
                        
                        if param.min_value is not None and numeric_value < param.min_value:
                            raise ValueError(f"Parameter '{param.name}' must be >= {param.min_value}. Got: {value}")
                        
                        if param.max_value is not None and numeric_value > param.max_value:
                            raise ValueError(f"Parameter '{param.name}' must be <= {param.max_value}. Got: {value}")
                            
                    except (ValueError, TypeError) as e:
                        if "invalid literal" in str(e):
                            raise ValueError(f"Parameter '{param.name}' must be a valid {param.var_type}. Got: {value}")
                        raise
    
    def _get_safe_value(self, value: Any) -> str:
        """Convert value to safe shell string."""
        if value is None:
            return '""'  # Empty string for None values
        elif value is True:
            return 'true'
        elif value is False:
            return 'false'
        else:
            return shlex.quote(str(value))
    
    def _perform_substitutions(self, content: str, substitutions: Dict[str, str]) -> str:
        """Perform all substitutions in a single pass for better performance."""
        if not substitutions:
            return content
        
        try:
            # Sort patterns by length (longest first) to avoid partial matches
            patterns = sorted(substitutions.keys(), key=len, reverse=True)
            
            # Build combined regex pattern
            escaped_patterns = [re.escape(pattern) for pattern in patterns]
            combined_pattern = '|'.join(f'({pattern})' for pattern in escaped_patterns)
            
            def replace_match(match):
                matched_text = match.group(0)
                return substitutions[matched_text]
            
            return re.sub(combined_pattern, replace_match, content)
        except re.error as e:
            raise ValueError(f"Failed to perform parameter substitutions: {e}")
        except Exception as e:
            raise ValueError(f"Unexpected error during parameter substitution: {e}")
    
    def get_help(self) -> str:
        """Get help text."""
        parser = self.create_parser()
        if not parser:
            return f"✨ {self.path.name} - No parameters required"
        
        import io
        help_buffer = io.StringIO()
        parser.print_help(help_buffer)
        return help_buffer.getvalue()


# Public API functions
def analyze_bash_magic(context: AnalysisContext) -> None:
    """Integrate bash magic into the analysis pipeline."""
    if context.get('lang') != 'shell':
        return
    
    script = BashScript(context.script_path, context.content)
    
    context.set_nested('bash_magic.script', script)
    context.set_nested('bash_magic.has_parameters', script.has_parameters)
    context.set_nested('bash_magic.parameters', [
        {
            'name': p.name,
            'type': p.type,
            'position': p.position,
            'flag': p.flag,
            'description': p.description,
            'required': p.required,
            'var_type': p.var_type,
            'default': p.default
        }
        for p in script.parameters
    ])


def compile_bash_magic(context: AnalysisContext, args: List[str]) -> Optional[str]:
    """Compile bash script with parameter magic."""
    bash_magic = context.get_nested('bash_magic.script')
    if not bash_magic or not isinstance(bash_magic, BashScript):
        return None
    
    if not bash_magic.has_parameters:
        return None
    
    param_values = bash_magic.parse_args(args)
    if param_values is None:
        return None
    
    return bash_magic.compile_with_params(param_values)


def get_bash_help(context: AnalysisContext) -> Optional[str]:
    """Get help text for bash script."""
    bash_magic = context.get_nested('bash_magic.script')
    if not bash_magic or not isinstance(bash_magic, BashScript):
        return None
    
    return bash_magic.get_help()


def create_bash_magic(script_path: Path) -> BashScript:
    """Create bash magic directly from a script path."""
    with open(script_path, 'r') as f:
        content = f.read()
    return BashScript(script_path, content)


# Simple wrapper functions for testing and direct usage
def analyze_bash_script(content: str) -> Dict[str, Any]:
    """Analyze a bash script and return parameter information."""
    script = BashScript(Path("test.sh"), content)
    return {
        'positional_refs': {p.position for p in script.parameters if p.type == 'positional'},
        'undefined_vars': {p.name for p in script.parameters if p.type == 'option'},
        'parameters': script.parameters,
        'has_parameters': script.has_parameters
    }


def compile_bash_script(content: str, param_values: Dict[str, Any]) -> str:
    """Compile a bash script with parameter substitution."""
    script = BashScript(Path("test.sh"), content)
    return script.compile_with_params(param_values)