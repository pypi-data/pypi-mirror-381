"""
🌟 UNIFIED PARAMETER PARSER 🌟
A comprehensive system for parsing parameter metadata from various formats.

Supports:
- Docstring formats (Google, NumPy, Sphinx)
- Bash USAGE lines
- Argparse help strings
- Legacy colon-separated format
- Custom format detection and parsing

This component provides a unified interface for extracting parameter information
from any supported format, making it easy to work with different documentation styles.
"""

import re
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union, Any, Type
from enum import Enum


class ParameterType(Enum):
    """Supported parameter types."""
    STR = "str"
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"
    PATH = "path"
    LIST = "list"


class ArgumentType(Enum):
    """Types of arguments."""
    POSITIONAL = "positional"
    OPTION = "option"
    FLAG = "flag"


@dataclass
class ParameterInfo:
    """Unified parameter information container."""
    name: str
    arg_type: ArgumentType = ArgumentType.OPTION
    param_type: ParameterType = ParameterType.STR
    description: str = ""
    default: Optional[Any] = None
    required: bool = True
    choices: Optional[List[str]] = None
    min_value: Optional[Union[int, float]] = None
    max_value: Optional[Union[int, float]] = None
    position: Optional[int] = None
    flag: Optional[str] = None
    aliases: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        """Auto-generate missing fields."""
        if self.arg_type == ArgumentType.OPTION and not self.flag:
            self.flag = f"--{self.name.lower().replace('_', '-')}"
        elif self.arg_type == ArgumentType.FLAG and not self.flag:
            self.flag = f"--{self.name.lower().replace('_', '-')}"


@dataclass
class ParseResult:
    """Result of parameter parsing."""
    parameters: List[ParameterInfo] = field(default_factory=list)
    usage_line: Optional[str] = None
    description: Optional[str] = None
    format_detected: Optional[str] = None
    confidence: float = 0.0
    
    def get_parameter(self, name: str) -> Optional[ParameterInfo]:
        """Get parameter by name."""
        return next((p for p in self.parameters if p.name == name), None)
    
    def get_positional_parameters(self) -> List[ParameterInfo]:
        """Get all positional parameters sorted by position."""
        positional = [p for p in self.parameters if p.arg_type == ArgumentType.POSITIONAL]
        return sorted(positional, key=lambda p: p.position or 0)
    
    def get_option_parameters(self) -> List[ParameterInfo]:
        """Get all option parameters."""
        return [p for p in self.parameters if p.arg_type == ArgumentType.OPTION]
    
    def get_flag_parameters(self) -> List[ParameterInfo]:
        """Get all flag parameters."""
        return [p for p in self.parameters if p.arg_type == ArgumentType.FLAG]


class ParameterParser(ABC):
    """Abstract base class for parameter parsers."""
    
    @abstractmethod
    def can_parse(self, content: str) -> float:
        """
        Check if this parser can handle the given content.
        
        Returns:
            Confidence score (0.0 to 1.0) indicating how well this parser
            can handle the content. Higher scores indicate better matches.
        """
        pass
    
    @abstractmethod
    def parse(self, content: str) -> ParseResult:
        """
        Parse parameter information from the content.
        
        Args:
            content: The text content to parse
            
        Returns:
            ParseResult containing extracted parameter information
        """
        pass
    
    @property
    @abstractmethod
    def format_name(self) -> str:
        """Name of the format this parser handles."""
        pass


class DocstringParser(ParameterParser):
    """Parser for various docstring formats (Google, NumPy, Sphinx)."""
    
    def __init__(self):
        # Google-style patterns
        self.google_args_pattern = r'Args:\s*\n((?:\s*\w+.*\n?)*)'
        self.google_param_pattern = r'\s*(\w+)\s*\(([^)]+)\):\s*([^.\n]+)\.?\s*(?:Default:\s*([^.\n]+)\.?)?\s*(?:Required:\s*(true|false)\.?)?\s*(?:Choices:\s*\[([^\]]+)\]\.?)?\s*(?:Range:\s*(\d+(?:\.\d+)?)-(\d+(?:\.\d+)?)\.?)?'
        
        # NumPy-style patterns
        self.numpy_params_pattern = r'Parameters\s*\n\s*-+\s*\n((?:.*\n?)*?)(?=\n\s*(?:Returns|Notes|Examples|\Z))'
        self.numpy_param_pattern = r'(\w+)\s*:\s*([^,\n]+)(?:,\s*optional)?\s*\n\s*([^\n]+)'
        
        # Sphinx-style patterns
        self.sphinx_param_pattern = r':param\s+(?:(\w+)\s+)?(\w+):\s*([^\n]+)'
        self.sphinx_type_pattern = r':type\s+(\w+):\s*([^\n]+)'
        
        # Direct format (no heading)
        self.direct_param_pattern = r'#\s*(\w+)\s*\(([^)]+)\):\s*([^.\n]+)\.?\s*(?:Default:\s*([^.\n]+)\.?)?\s*(?:Required:\s*(true|false)\.?)?\s*(?:Choices:\s*\[([^\]]+)\]\.?)?\s*(?:Range:\s*(\d+(?:\.\d+)?)-(\d+(?:\.\d+)?)\.?)?'
    
    @property
    def format_name(self) -> str:
        return "docstring"
    
    def can_parse(self, content: str) -> float:
        """Check if content contains docstring-style parameter documentation."""
        confidence = 0.0
        
        # Check for Google-style Args:
        if re.search(self.google_args_pattern, content, re.MULTILINE):
            confidence = max(confidence, 0.9)
        
        # Check for NumPy-style Parameters
        if re.search(self.numpy_params_pattern, content, re.MULTILINE):
            confidence = max(confidence, 0.9)
        
        # Check for Sphinx-style :param:
        if re.search(self.sphinx_param_pattern, content):
            confidence = max(confidence, 0.9)
        
        # Check for direct parameter format
        if re.search(self.direct_param_pattern, content):
            confidence = max(confidence, 0.8)
        
        # Check for parameter-like patterns
        param_indicators = [
            r'\w+\s*\([^)]+\):\s*[^.\n]+',  # name (type): description
            r':param\s+\w+:',               # :param name:
            r'Args:\s*\n',                  # Args:
            r'Parameters\s*\n\s*-+'         # Parameters\n----
        ]
        
        for pattern in param_indicators:
            if re.search(pattern, content):
                confidence = max(confidence, 0.6)
        
        return confidence
    
    def parse(self, content: str) -> ParseResult:
        """Parse docstring-style parameter documentation."""
        result = ParseResult(format_detected=self.format_name)
        
        # Try Google-style first
        google_result = self._parse_google_style(content)
        if google_result.parameters:
            result.parameters.extend(google_result.parameters)
            result.confidence = max(result.confidence, 0.9)
        
        # Try direct format
        direct_result = self._parse_direct_format(content)
        if direct_result.parameters:
            # Merge with existing parameters, avoiding duplicates
            existing_names = {p.name for p in result.parameters}
            for param in direct_result.parameters:
                if param.name not in existing_names:
                    result.parameters.append(param)
            result.confidence = max(result.confidence, 0.8)
        
        # Try NumPy-style
        numpy_result = self._parse_numpy_style(content)
        if numpy_result.parameters:
            existing_names = {p.name for p in result.parameters}
            for param in numpy_result.parameters:
                if param.name not in existing_names:
                    result.parameters.append(param)
            result.confidence = max(result.confidence, 0.9)
        
        # Try Sphinx-style
        sphinx_result = self._parse_sphinx_style(content)
        if sphinx_result.parameters:
            existing_names = {p.name for p in result.parameters}
            for param in sphinx_result.parameters:
                if param.name not in existing_names:
                    result.parameters.append(param)
            result.confidence = max(result.confidence, 0.9)
        
        return result
    
    def _parse_google_style(self, content: str) -> ParseResult:
        """Parse Google-style docstring parameters."""
        result = ParseResult()
        
        # Find Args: section
        args_match = re.search(self.google_args_pattern, content, re.MULTILINE)
        if not args_match:
            return result
        
        args_section = args_match.group(1)
        
        # Parse individual parameters
        for match in re.finditer(self.google_param_pattern, args_section):
            param = self._create_parameter_from_google_match(match)
            if param:
                result.parameters.append(param)
        
        return result
    
    def _parse_direct_format(self, content: str) -> ParseResult:
        """Parse direct parameter format (no Args: heading)."""
        result = ParseResult()
        
        for match in re.finditer(self.direct_param_pattern, content):
            param = self._create_parameter_from_google_match(match)
            if param:
                result.parameters.append(param)
        
        return result
    
    def _parse_numpy_style(self, content: str) -> ParseResult:
        """Parse NumPy-style docstring parameters."""
        result = ParseResult()
        
        params_match = re.search(self.numpy_params_pattern, content, re.MULTILINE | re.DOTALL)
        if not params_match:
            return result
        
        params_section = params_match.group(1)
        
        for match in re.finditer(self.numpy_param_pattern, params_section):
            name = match.group(1)
            type_info = match.group(2).strip()
            description = match.group(3).strip()
            
            param = ParameterInfo(
                name=name,
                param_type=self._parse_type(type_info),
                description=description,
                required='optional' not in type_info.lower()
            )
            result.parameters.append(param)
        
        return result
    
    def _parse_sphinx_style(self, content: str) -> ParseResult:
        """Parse Sphinx-style docstring parameters."""
        result = ParseResult()
        params = {}
        
        # Parse :param: directives
        for match in re.finditer(self.sphinx_param_pattern, content):
            param_type = match.group(1)
            param_name = match.group(2)
            description = match.group(3).strip()
            
            if param_name not in params:
                params[param_name] = ParameterInfo(name=param_name, description=description)
            
            if param_type:
                params[param_name].param_type = self._parse_type(param_type)
        
        # Parse :type: directives
        for match in re.finditer(self.sphinx_type_pattern, content):
            param_name = match.group(1)
            type_info = match.group(2).strip()
            
            if param_name not in params:
                params[param_name] = ParameterInfo(name=param_name)
            
            params[param_name].param_type = self._parse_type(type_info)
        
        result.parameters = list(params.values())
        return result
    
    def _create_parameter_from_google_match(self, match) -> Optional[ParameterInfo]:
        """Create ParameterInfo from Google-style regex match."""
        name = match.group(1)
        type_str = match.group(2) if len(match.groups()) > 1 else 'str'
        description = match.group(3).strip() if len(match.groups()) > 2 else ''
        default = match.group(4).strip() if len(match.groups()) > 3 and match.group(4) else None
        required = match.group(5) == 'true' if len(match.groups()) > 4 and match.group(5) else (default is None)
        choices_str = match.group(6) if len(match.groups()) > 5 else None
        min_val = match.group(7) if len(match.groups()) > 6 else None
        max_val = match.group(8) if len(match.groups()) > 7 else None
        
        choices = None
        if choices_str:
            choices = [c.strip() for c in choices_str.split(',')]
        
        param_type = self._parse_type(type_str)
        
        return ParameterInfo(
            name=name,
            param_type=param_type,
            description=description,
            default=self._parse_default_value(default, param_type),
            required=required,
            choices=choices,
            min_value=self._parse_numeric_value(min_val, param_type),
            max_value=self._parse_numeric_value(max_val, param_type)
        )
    
    def _parse_type(self, type_str: str) -> ParameterType:
        """Parse type string to ParameterType enum."""
        type_str = type_str.lower().strip()
        
        type_mapping = {
            'str': ParameterType.STR,
            'string': ParameterType.STR,
            'int': ParameterType.INT,
            'integer': ParameterType.INT,
            'float': ParameterType.FLOAT,
            'double': ParameterType.FLOAT,
            'bool': ParameterType.BOOL,
            'boolean': ParameterType.BOOL,
            'path': ParameterType.PATH,
            'file': ParameterType.PATH,
            'list': ParameterType.LIST,
            'array': ParameterType.LIST
        }
        
        return type_mapping.get(type_str, ParameterType.STR)
    
    def _parse_default_value(self, default_str: Optional[str], param_type: ParameterType) -> Optional[Any]:
        """Parse default value string to appropriate type."""
        if not default_str:
            return None
        
        default_str = default_str.strip()
        
        if param_type == ParameterType.BOOL:
            return default_str.lower() in ['true', '1', 'yes', 'on']
        elif param_type == ParameterType.INT:
            try:
                return int(default_str)
            except ValueError:
                return None
        elif param_type == ParameterType.FLOAT:
            try:
                return float(default_str)
            except ValueError:
                return None
        else:
            return default_str
    
    def _parse_numeric_value(self, value_str: Optional[str], param_type: ParameterType) -> Optional[Union[int, float]]:
        """Parse numeric value for min/max constraints."""
        if not value_str:
            return None
        
        try:
            if param_type == ParameterType.INT:
                return int(value_str)
            elif param_type == ParameterType.FLOAT:
                return float(value_str)
        except ValueError:
            pass
        
        return None


class UsageLineParser(ParameterParser):
    """Parser for bash USAGE lines and similar command-line usage patterns."""
    
    def __init__(self):
        # Common usage line patterns
        self.usage_patterns = [
            r'USAGE:\s*(.+)',
            r'Usage:\s*(.+)',
            r'usage:\s*(.+)',
            r'# USAGE:\s*(.+)',
            r'# Usage:\s*(.+)',
            r'# usage:\s*(.+)'
        ]
        
        # Pattern to extract command structure
        self.command_pattern = r'(\w+)\s+(.*)'
        
        # Patterns for different argument types
        self.positional_pattern = r'([A-Z_][A-Z0-9_]*)'
        self.optional_pattern = r'\[([^\]]+)\]'
        self.flag_pattern = r'--(\w+(?:-\w+)*)'
        self.short_flag_pattern = r'-([a-zA-Z])'
    
    @property
    def format_name(self) -> str:
        return "usage_line"
    
    def can_parse(self, content: str) -> float:
        """Check if content contains usage line patterns."""
        for pattern in self.usage_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                return 0.8
        
        # Check for usage-like patterns
        usage_indicators = [
            r'\w+\s+[A-Z_]+',  # command ARGUMENT
            r'--\w+',          # --option
            r'\[[^\]]+\]'      # [optional]
        ]
        
        confidence = 0.0
        for pattern in usage_indicators:
            if re.search(pattern, content):
                confidence += 0.2
        
        return min(confidence, 0.6)
    
    def parse(self, content: str) -> ParseResult:
        """Parse usage line to extract parameter information."""
        result = ParseResult(format_detected=self.format_name)
        
        # Find usage line
        usage_line = None
        for pattern in self.usage_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                usage_line = match.group(1).strip()
                result.usage_line = usage_line
                break
        
        if not usage_line:
            return result
        
        # Parse command structure
        cmd_match = re.match(self.command_pattern, usage_line)
        if not cmd_match:
            return result
        
        command = cmd_match.group(1)
        args_part = cmd_match.group(2)
        
        position = 1
        
        # Extract positional arguments
        for match in re.finditer(self.positional_pattern, args_part):
            arg_name = match.group(1).lower()
            param = ParameterInfo(
                name=arg_name,
                arg_type=ArgumentType.POSITIONAL,
                position=position,
                description=f"{arg_name} (positional argument {position})"
            )
            result.parameters.append(param)
            position += 1
        
        # Extract flags and options
        for match in re.finditer(self.flag_pattern, args_part):
            flag_name = match.group(1).replace('-', '_')
            param = ParameterInfo(
                name=flag_name,
                arg_type=ArgumentType.OPTION,
                flag=f"--{match.group(1)}",
                description=f"Value for --{match.group(1)}"
            )
            result.parameters.append(param)
        
        # Extract short flags
        for match in re.finditer(self.short_flag_pattern, args_part):
            flag_char = match.group(1)
            param = ParameterInfo(
                name=f"flag_{flag_char}",
                arg_type=ArgumentType.FLAG,
                flag=f"-{flag_char}",
                description=f"Flag -{flag_char}"
            )
            result.parameters.append(param)
        
        result.confidence = 0.8 if result.parameters else 0.3
        return result


class LegacyColonParser(ParameterParser):
    """Parser for legacy colon-separated format."""
    
    def __init__(self):
        self.colon_pattern = r'#\s*([^:\s]+):([^:\s]*):([^:]*):([^:]*):([^:]*):?([^:]*)?:?([^:]*)?:?([^:]*)?'
    
    @property
    def format_name(self) -> str:
        return "legacy_colon"
    
    def can_parse(self, content: str) -> float:
        """Check if content contains legacy colon format."""
        matches = list(re.finditer(self.colon_pattern, content))
        if matches:
            # Higher confidence if multiple parameters found
            return min(0.7 + len(matches) * 0.1, 1.0)
        return 0.0
    
    def parse(self, content: str) -> ParseResult:
        """Parse legacy colon-separated format."""
        result = ParseResult(format_detected=self.format_name)
        
        for match in re.finditer(self.colon_pattern, content):
            name = match.group(1)
            type_str = match.group(2) or 'str'
            description = match.group(3) or ''
            default = match.group(4) or None
            required_str = match.group(5) or 'true'
            choices_str = match.group(6) or None
            min_val = match.group(7) or None
            max_val = match.group(8) or None
            
            param_type = self._parse_type(type_str)
            required = required_str.lower() not in ['false', 'no', '0', '']
            choices = choices_str.split(',') if choices_str else None
            
            param = ParameterInfo(
                name=name,
                param_type=param_type,
                description=description,
                default=self._parse_default_value(default, param_type),
                required=required,
                choices=choices,
                min_value=self._parse_numeric_value(min_val, param_type),
                max_value=self._parse_numeric_value(max_val, param_type)
            )
            result.parameters.append(param)
        
        result.confidence = 0.7 if result.parameters else 0.0
        return result
    
    def _parse_type(self, type_str: str) -> ParameterType:
        """Parse type string to ParameterType enum."""
        type_mapping = {
            'str': ParameterType.STR,
            'int': ParameterType.INT,
            'float': ParameterType.FLOAT,
            'bool': ParameterType.BOOL,
            'path': ParameterType.PATH
        }
        return type_mapping.get(type_str.lower(), ParameterType.STR)
    
    def _parse_default_value(self, default_str: Optional[str], param_type: ParameterType) -> Optional[Any]:
        """Parse default value string to appropriate type."""
        if not default_str:
            return None
        
        if param_type == ParameterType.BOOL:
            return default_str.lower() in ['true', '1', 'yes']
        elif param_type == ParameterType.INT:
            try:
                return int(default_str)
            except ValueError:
                return None
        elif param_type == ParameterType.FLOAT:
            try:
                return float(default_str)
            except ValueError:
                return None
        else:
            return default_str
    
    def _parse_numeric_value(self, value_str: Optional[str], param_type: ParameterType) -> Optional[Union[int, float]]:
        """Parse numeric value for constraints."""
        if not value_str:
            return None
        
        try:
            if param_type == ParameterType.INT:
                return int(value_str)
            elif param_type == ParameterType.FLOAT:
                return float(value_str)
        except ValueError:
            pass
        
        return None


class UnifiedParameterParser:
    """
    Unified parameter parser that can handle multiple formats.
    
    Automatically detects the best parser for the given content and
    provides a consistent interface for parameter extraction.
    """
    
    def __init__(self):
        self.parsers: List[ParameterParser] = [
            DocstringParser(),
            UsageLineParser(),
            LegacyColonParser()
        ]
    
    def register_parser(self, parser: ParameterParser):
        """Register a new parser."""
        self.parsers.append(parser)
    
    def parse(self, content: str) -> ParseResult:
        """
        Parse parameter information from content using the best available parser.
        
        Args:
            content: Text content to parse
            
        Returns:
            ParseResult with extracted parameter information
        """
        best_parser = None
        best_confidence = 0.0
        
        # Find the parser with highest confidence
        for parser in self.parsers:
            confidence = parser.can_parse(content)
            if confidence > best_confidence:
                best_confidence = confidence
                best_parser = parser
        
        if best_parser is None:
            return ParseResult(confidence=0.0)
        
        # Parse with the best parser
        result = best_parser.parse(content)
        result.confidence = best_confidence
        
        # Try to enhance with other parsers if confidence is not perfect
        if best_confidence < 1.0:
            self._enhance_with_other_parsers(content, result, best_parser)
        
        return result
    
    def parse_with_all(self, content: str) -> Dict[str, ParseResult]:
        """
        Parse content with all available parsers.
        
        Returns:
            Dictionary mapping parser names to their results
        """
        results = {}
        for parser in self.parsers:
            if parser.can_parse(content) > 0:
                results[parser.format_name] = parser.parse(content)
        return results
    
    def _enhance_with_other_parsers(self, content: str, result: ParseResult, primary_parser: ParameterParser):
        """Try to enhance the result with information from other parsers."""
        existing_names = {p.name for p in result.parameters}
        
        for parser in self.parsers:
            if parser == primary_parser:
                continue
            
            if parser.can_parse(content) > 0.3:  # Only use parsers with reasonable confidence
                other_result = parser.parse(content)
                
                # Add parameters that don't already exist
                for param in other_result.parameters:
                    if param.name not in existing_names:
                        result.parameters.append(param)
                        existing_names.add(param.name)
                
                # Use usage line if we don't have one
                if not result.usage_line and other_result.usage_line:
                    result.usage_line = other_result.usage_line