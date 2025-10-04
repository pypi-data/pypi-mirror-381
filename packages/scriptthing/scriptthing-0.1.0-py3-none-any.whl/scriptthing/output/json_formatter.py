"""
JSON output formatter for scriptthing.

Provides JSON output with configurable indentation and formatting options.
"""

import json
from typing import Any, Dict, List, Optional
from datetime import datetime, date
from decimal import Decimal
from .base import OutputFormatter, ConfigurableFormatter


class JSONFormatter(ConfigurableFormatter):
    """
    JSON formatter with customizable output options.
    """
    
    DEFAULT_CONFIG = {
        'indent': 2,
        'sort_keys': False,
        'ensure_ascii': False,
        'separators': None,  # Use default (',', ': ')
        'compact': False,
        'serialize_datetime': True,
        'datetime_format': 'iso',  # 'iso', 'timestamp', or custom format string
        'handle_nan': True,
        'allow_nan': False,
    }
    
    def get_content_type(self) -> str:
        return 'application/json'
    
    def get_file_extension(self) -> str:
        return 'json'
    
    def format_data(self, data: Any) -> str:
        """
        Format data as JSON with configured options.
        """
        # Prepare data for JSON serialization
        serializable_data = self._prepare_for_json(data)
        
        # Configure JSON dumping options
        json_options = {
            'ensure_ascii': self.config['ensure_ascii'],
            'sort_keys': self.config['sort_keys'],
            'allow_nan': self.config['allow_nan'],
        }
        
        # Handle compact vs. pretty printing
        if self.config['compact']:
            json_options['separators'] = (',', ':')
            json_options['indent'] = None
        else:
            json_options['indent'] = self.config['indent']
            if self.config['separators']:
                json_options['separators'] = self.config['separators']
        
        try:
            return json.dumps(serializable_data, **json_options)
        except (TypeError, ValueError) as e:
            # Fallback for non-serializable data
            return json.dumps({
                'error': 'JSON serialization failed',
                'message': str(e),
                'data_type': str(type(data).__name__),
                'data_repr': repr(data)[:500]  # Truncate for safety
            }, **json_options)
    
    def _prepare_for_json(self, obj: Any) -> Any:
        """
        Recursively prepare an object for JSON serialization.
        """
        if obj is None or isinstance(obj, (bool, int, float, str)):
            return obj
        
        # Handle NaN and infinity
        if isinstance(obj, float):
            if self.config['handle_nan']:
                if obj != obj:  # NaN check
                    return None
                elif obj == float('inf'):
                    return "Infinity"
                elif obj == float('-inf'):
                    return "-Infinity"
            return obj
        
        # Handle datetime objects
        if isinstance(obj, (datetime, date)):
            if self.config['serialize_datetime']:
                return self._format_datetime(obj)
            else:
                return str(obj)
        
        # Handle Decimal
        if isinstance(obj, Decimal):
            return float(obj)
        
        # Handle dictionaries
        if isinstance(obj, dict):
            return {
                str(key): self._prepare_for_json(value)
                for key, value in obj.items()
            }
        
        # Handle lists and tuples
        if isinstance(obj, (list, tuple)):
            return [self._prepare_for_json(item) for item in obj]
        
        # Handle sets
        if isinstance(obj, set):
            return list(obj)
        
        # For other types, try to convert to string
        try:
            # Try to see if the object has a custom JSON representation
            if hasattr(obj, '__dict__'):
                return self._prepare_for_json(obj.__dict__)
            else:
                return str(obj)
        except Exception:
            return f"<{type(obj).__name__} object>"
    
    def _format_datetime(self, dt: datetime) -> str:
        """Format datetime objects according to configuration."""
        if self.config['datetime_format'] == 'iso':
            return dt.isoformat()
        elif self.config['datetime_format'] == 'timestamp':
            return dt.timestamp()
        else:
            # Custom format string
            try:
                return dt.strftime(self.config['datetime_format'])
            except (ValueError, TypeError):
                return dt.isoformat()





class JSONLinesFormatter(OutputFormatter):
    """
    JSON Lines formatter - each item on a separate line as JSON.
    
    Useful for streaming data or when you have a list of objects
    that should each be on their own line.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.item_formatter = CompactJSONFormatter(**kwargs)
    
    def get_content_type(self) -> str:
        return 'application/jsonl'
    
    def get_file_extension(self) -> str:
        return 'jsonl'
    
    def format_data(self, data: Any) -> str:
        """
        Format data as JSON Lines.
        """
        if isinstance(data, list):
            lines = []
            for item in data:
                lines.append(self.item_formatter.format_data(item))
            return '\n'.join(lines)
        else:
            # Single item
            return self.item_formatter.format_data(data)
    
    def format_table(self, data: List[Dict[str, Any]], headers: Optional[List[str]] = None) -> str:
        """
        Format table data as JSON Lines (one object per row).
        """
        return self.format_data(data)


