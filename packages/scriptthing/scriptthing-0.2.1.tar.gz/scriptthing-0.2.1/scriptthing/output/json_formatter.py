"""
JSON output formatter for scriptthing.
"""

import json
from typing import Any, Dict, List
from datetime import datetime, date
from .base import OutputFormatter


class JSONFormatter(OutputFormatter):
    """JSON formatter with configurable options."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.indent = kwargs.get('indent', 2)
        self.compact = kwargs.get('compact', False)
        self.jsonlines = kwargs.get('jsonlines', False)
    
    def get_content_type(self) -> str:
        return 'application/json'
    
    def get_file_extension(self) -> str:
        return 'json'
    
    def format_data(self, data: Any) -> str:
        """Format data as JSON."""
        if self.jsonlines and isinstance(data, list):
            return '\n'.join(json.dumps(self._prepare_for_json(item), indent=None, separators=(',', ':')) 
                           for item in data)
        
        serializable_data = self._prepare_for_json(data)
        if self.compact:
            return json.dumps(serializable_data, separators=(',', ':'))
        return json.dumps(serializable_data, indent=self.indent)
    
    def _prepare_for_json(self, obj: Any) -> Any:
        """Prepare object for JSON serialization."""
        if obj is None or isinstance(obj, (bool, int, float, str)):
            return obj
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, dict):
            return {str(k): self._prepare_for_json(v) for k, v in obj.items()}
        if isinstance(obj, (list, tuple, set)):
            return [self._prepare_for_json(item) for item in obj]
        return str(obj)



# Alias for backwards compatibility
JSONLinesFormatter = lambda **kwargs: JSONFormatter(jsonlines=True, **kwargs)
