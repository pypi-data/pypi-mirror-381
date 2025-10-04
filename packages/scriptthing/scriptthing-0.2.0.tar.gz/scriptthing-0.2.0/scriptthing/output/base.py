"""
Base classes and interfaces for scriptthing output formatters.

This module provides the foundational classes that all output formatters
must implement, ensuring a consistent API across different output formats.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union



class OutputFormatter(ABC):
    """Abstract base class for all output formatters."""
    
    def __init__(self, **kwargs):
        """Initialize the formatter with optional configuration."""
        self.config = kwargs
    
    @abstractmethod
    def format_data(self, data: Any) -> str:
        """
        Format the given data into a string representation.
        
        Args:
            data: The data to format (can be dict, list, primitive types, etc.)
            
        Returns:
            str: The formatted output string
        """
        pass
    
    @abstractmethod
    def get_content_type(self) -> str:
        """
        Get the MIME content type for this formatter's output.
        
        Returns:
            str: MIME content type (e.g., 'text/plain', 'application/json')
        """
        pass
    
    @abstractmethod
    def get_file_extension(self) -> str:
        """
        Get the recommended file extension for this format.
        
        Returns:
            str: File extension without the dot (e.g., 'txt', 'json')
        """
        pass
    
    def format_table(self, data: List[Dict[str, Any]], headers: Optional[List[str]] = None) -> str:
        """
        Format tabular data. Default implementation delegates to format_data.
        
        Args:
            data: List of dictionaries representing table rows
            headers: Optional list of column headers (if None, uses keys from first row)
            
        Returns:
            str: The formatted table string
        """
        if headers is None and data:
            headers = list(data[0].keys())
        
        table_data = {
            'headers': headers or [],
            'rows': data
        }
        return self.format_data(table_data)
    




class TableFormatter(OutputFormatter):
    """
    Specialized base class for formatters that work well with tabular data.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.show_headers = kwargs.get('show_headers', True)
        self.auto_headers = kwargs.get('auto_headers', True)
    
    def format_data(self, data: Any) -> str:
        """
        Format data, with special handling for table-like structures.
        """
        if isinstance(data, list) and data and isinstance(data[0], dict):
            # This looks like tabular data
            return self.format_table(data)
        elif isinstance(data, dict) and 'headers' in data and 'rows' in data:
            # This is explicitly structured table data
            return self.format_table(data['rows'], data['headers'])
        else:
            # Fall back to regular data formatting
            return self._format_non_table_data(data)
    
    @abstractmethod
    def _format_non_table_data(self, data: Any) -> str:
        """Format non-tabular data."""
        pass


class ConfigurableFormatter(OutputFormatter):
    """
    Base class for formatters that support extensive configuration.
    """
    
    DEFAULT_CONFIG = {}
    
    def __init__(self, **kwargs):
        # Merge default config with provided kwargs
        config = self.DEFAULT_CONFIG.copy()
        config.update(kwargs)
        super().__init__(**config)
    
    def update_config(self, **kwargs) -> None:
        """Update the formatter configuration."""
        self.config.update(kwargs)
    
    def get_config(self) -> Dict[str, Any]:
        """Get the current configuration."""
        return self.config.copy()


# Utility functions for common formatting tasks

def sanitize_filename(name: str) -> str:
    """
    Sanitize a string to be safe for use as a filename.
    
    Args:
        name: The original name
        
    Returns:
        str: A sanitized filename
    """
    import re
    # Replace unsafe characters with underscores
    safe_name = re.sub(r'[<>:"/\\|?*]', '_', name)
    # Remove any remaining problematic characters
    safe_name = re.sub(r'[^\w\-_.]', '_', safe_name)
    # Collapse multiple underscores
    safe_name = re.sub(r'_+', '_', safe_name)
    # Trim underscores from start/end
    return safe_name.strip('_')


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate a string to a maximum length, adding a suffix if truncated.
    
    Args:
        text: The original text
        max_length: Maximum allowed length
        suffix: Suffix to add if truncated
        
    Returns:
        str: The truncated string
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix