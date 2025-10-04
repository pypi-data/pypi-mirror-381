"""
YAML output formatter for scriptthing.

Provides YAML output with configurable formatting and style options.
"""

from typing import Any, Dict, List, Optional
from .base import OutputFormatter, ConfigurableFormatter

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


class YAMLFormatter(ConfigurableFormatter):
    """
    YAML formatter with customizable output options.
    
    Requires PyYAML to be installed.
    """
    
    DEFAULT_CONFIG = {
        'default_style': None,  # None, '"', "'", '>', '|'
        'default_flow_style': False,  # True for inline style
        'indent': 2,
        'width': 80,
        'allow_unicode': True,
        'line_break': None,  # None, '\r\n', '\r', '\n'
        'encoding': 'utf-8',
        'explicit_start': False,  # Start with ---
        'explicit_end': False,    # End with ...
        'version': None,  # YAML version
        'tags': None,
        'sort_keys': False,
        'safe_dump': True,  # Use safe_dump instead of dump
        'represent_none': 'null',  # How to represent None values
        'custom_representer': True,  # Use custom representers for special types
    }
    
    def __init__(self, **kwargs):
        if not HAS_YAML:
            raise ImportError("PyYAML is required for YAML formatting. Install with: pip install PyYAML")
        super().__init__(**kwargs)
        self._setup_yaml()
    
    def get_content_type(self) -> str:
        return 'application/yaml'
    
    def get_file_extension(self) -> str:
        return 'yaml'
    
    def format_data(self, data: Any) -> str:
        """
        Format data as YAML.
        """
        # Prepare data for YAML serialization
        prepared_data = self._prepare_for_yaml(data)
        
        # Configure YAML dumping options
        yaml_options = {
            'default_style': self.config['default_style'],
            'default_flow_style': self.config['default_flow_style'],
            'indent': self.config['indent'],
            'width': self.config['width'],
            'allow_unicode': self.config['allow_unicode'],
            'line_break': self.config['line_break'],
            'encoding': None,  # We'll handle encoding ourselves
            'explicit_start': self.config['explicit_start'],
            'explicit_end': self.config['explicit_end'],
            'version': self.config['version'],
            'tags': self.config['tags'],
            'sort_keys': self.config['sort_keys'],
        }
        
        # Remove None values from options
        yaml_options = {k: v for k, v in yaml_options.items() if v is not None}
        
        try:
            if self.config['safe_dump']:
                return yaml.safe_dump(prepared_data, **yaml_options)
            else:
                return yaml.dump(prepared_data, **yaml_options)
        except (yaml.YAMLError, TypeError) as e:
            # Fallback for problematic data
            fallback_data = {
                'error': 'YAML serialization failed',
                'message': str(e),
                'data_type': str(type(data).__name__),
                'data_repr': repr(data)[:500]  # Truncate for safety
            }
            return yaml.safe_dump(fallback_data, **yaml_options)
    
    def _setup_yaml(self):
        """Setup custom YAML representers."""
        if not self.config['custom_representer']:
            return
        
        # Custom representer for None values
        def represent_none(dumper, value):
            return dumper.represent_scalar('tag:yaml.org,2002:null', self.config['represent_none'])
        
        yaml.add_representer(type(None), represent_none)
        
        # Custom representer for sets
        def represent_set(dumper, value):
            return dumper.represent_list(list(value))
        
        yaml.add_representer(set, represent_set)
        
        # Custom representer for datetime objects
        try:
            from datetime import datetime, date
            
            def represent_datetime(dumper, value):
                return dumper.represent_scalar('tag:yaml.org,2002:timestamp', value.isoformat())
            
            def represent_date(dumper, value):
                return dumper.represent_scalar('tag:yaml.org,2002:timestamp', value.isoformat())
            
            yaml.add_representer(datetime, represent_datetime)
            yaml.add_representer(date, represent_date)
        except ImportError:
            pass
        
        # Custom representer for Decimal
        try:
            from decimal import Decimal
            
            def represent_decimal(dumper, value):
                return dumper.represent_scalar('tag:yaml.org,2002:float', str(value))
            
            yaml.add_representer(Decimal, represent_decimal)
        except ImportError:
            pass
    
    def _prepare_for_yaml(self, obj: Any) -> Any:
        """
        Recursively prepare an object for YAML serialization.
        """
        if obj is None or isinstance(obj, (bool, int, float, str)):
            return obj
        
        # Handle datetime objects
        if hasattr(obj, 'isoformat'):  # datetime-like objects
            return obj.isoformat()
        
        # Handle sets
        if isinstance(obj, set):
            return list(obj)
        
        # Handle dictionaries
        if isinstance(obj, dict):
            return {
                str(key): self._prepare_for_yaml(value)
                for key, value in obj.items()
            }
        
        # Handle lists and tuples
        if isinstance(obj, (list, tuple)):
            return [self._prepare_for_yaml(item) for item in obj]
        
        # For other types, try to convert to a serializable form
        try:
            if hasattr(obj, '__dict__'):
                return self._prepare_for_yaml(obj.__dict__)
            elif hasattr(obj, '_asdict'):  # namedtuple
                return self._prepare_for_yaml(obj._asdict())
            else:
                return str(obj)
        except Exception:
            return f"<{type(obj).__name__} object>"
    
    def format_table(self, data: List[Dict[str, Any]], headers: Optional[List[str]] = None) -> str:
        """
        Format table data as YAML.
        """
        if not data:
            return self.format_data([])
        
        # For tables, we can either output as a list of objects
        # or as a structured table with headers and rows
        if headers:
            table_structure = {
                'headers': headers,
                'rows': data
            }
            return self.format_data(table_structure)
        else:
            return self.format_data(data)


class CompactYAMLFormatter(YAMLFormatter):
    """
    Compact YAML formatter with flow style.
    """
    
    DEFAULT_CONFIG = {
        **YAMLFormatter.DEFAULT_CONFIG,
        'default_flow_style': True,
        'width': 200,
        'indent': 1,
    }


class VerboseYAMLFormatter(YAMLFormatter):
    """
    Verbose YAML formatter with explicit markers and sorting.
    """
    
    DEFAULT_CONFIG = {
        **YAMLFormatter.DEFAULT_CONFIG,
        'explicit_start': True,
        'explicit_end': True,
        'sort_keys': True,
        'indent': 4,
        'width': 120,
    }


class LiteralYAMLFormatter(YAMLFormatter):
    """
    YAML formatter that uses literal style for strings.
    """
    
    DEFAULT_CONFIG = {
        **YAMLFormatter.DEFAULT_CONFIG,
        'default_style': '|',  # Literal style
        'width': 120,
    }


class FoldedYAMLFormatter(YAMLFormatter):
    """
    YAML formatter that uses folded style for strings.
    """
    
    DEFAULT_CONFIG = {
        **YAMLFormatter.DEFAULT_CONFIG,
        'default_style': '>',  # Folded style
        'width': 80,
    }


# Fallback formatter when PyYAML is not available
class FallbackYAMLFormatter(ConfigurableFormatter):
    """
    Fallback YAML formatter that creates basic YAML-like output without PyYAML.
    
    This provides a basic implementation when PyYAML is not available.
    """
    
    DEFAULT_CONFIG = {
        'indent': 2,
        'sort_keys': False,
        'explicit_start': False,
        'explicit_end': False,
    }
    
    def get_content_type(self) -> str:
        return 'text/plain'  # Not real YAML
    
    def get_file_extension(self) -> str:
        return 'yaml'
    
    def format_data(self, data: Any) -> str:
        """
        Format data as basic YAML-like output.
        """
        lines = []
        
        if self.config['explicit_start']:
            lines.append('---')
        
        lines.append(self._format_value(data, 0))
        
        if self.config['explicit_end']:
            lines.append('...')
        
        return '\n'.join(lines)
    
    def _format_value(self, value: Any, level: int) -> str:
        """Format a value at the given indentation level."""
        indent = ' ' * (level * self.config['indent'])
        
        if value is None:
            return f"{indent}null"
        elif isinstance(value, bool):
            return f"{indent}{str(value).lower()}"
        elif isinstance(value, (int, float)):
            return f"{indent}{value}"
        elif isinstance(value, str):
            # Simple string handling - doesn't handle complex cases
            if '\n' in value:
                lines = [f"{indent}|"]
                for line in value.split('\n'):
                    lines.append(f"{indent}  {line}")
                return '\n'.join(lines)
            elif any(char in value for char in [':', '[', ']', '{', '}', '"', "'"]):
                # Need to quote
                escaped = value.replace('"', '\\"')
                return f'{indent}"{escaped}"'
            else:
                return f"{indent}{value}"
        elif isinstance(value, list):
            if not value:
                return f"{indent}[]"
            
            lines = []
            for item in value:
                if isinstance(item, (dict, list)):
                    lines.append(f"{indent}-")
                    item_lines = self._format_value(item, level + 1).split('\n')
                    for i, line in enumerate(item_lines):
                        if i == 0:
                            lines.append(f"{indent}  {line.strip()}")
                        else:
                            lines.append(line)
                else:
                    item_str = self._format_value(item, 0).strip()
                    lines.append(f"{indent}- {item_str}")
            return '\n'.join(lines)
        
        elif isinstance(value, dict):
            if not value:
                return f"{indent}{{}}"
            
            lines = []
            items = sorted(value.items()) if self.config['sort_keys'] else value.items()
            
            for key, val in items:
                key_str = str(key)
                if isinstance(val, (dict, list)) and val:
                    lines.append(f"{indent}{key_str}:")
                    val_lines = self._format_value(val, level + 1)
                    lines.append(val_lines)
                else:
                    val_str = self._format_value(val, 0).strip()
                    lines.append(f"{indent}{key_str}: {val_str}")
            
            return '\n'.join(lines)
        
        else:
            return f"{indent}{str(value)}"


# Export the appropriate formatter based on availability
if HAS_YAML:
    DefaultYAMLFormatter = YAMLFormatter
else:
    DefaultYAMLFormatter = FallbackYAMLFormatter