"""
Output manager for scriptthing.

Provides a unified interface for selecting and using different output formatters.
"""

from typing import Any, Dict, List, Optional, Type, Union
from io import StringIO
import os

from .base import OutputFormatter
from .text import TextFormatter
from .json_formatter import JSONFormatter, JSONLinesFormatter
from .csv import CSVFormatter, TSVFormatter, ExcelCSVFormatter, PipeDelimitedFormatter
from .xml import XMLFormatter, CompactXMLFormatter, AttributeXMLFormatter
from .html import HTMLFormatter, MinimalHTMLFormatter, BootstrapHTMLFormatter
from .markdown import MarkdownFormatter, GitHubMarkdownFormatter, SimpleMarkdownFormatter
from .yaml_formatter import DefaultYAMLFormatter

try:
    from .yaml_formatter import YAMLFormatter, CompactYAMLFormatter, VerboseYAMLFormatter
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


class OutputManager:
    """
    Central registry for output formatters.
    
    Provides access to all available formatters and format detection utilities.
    Used internally by the Output class for rendering operations.
    """
    
    def __init__(self):
        self._formatters = self._register_formatters()
        self._default_format = 'text'
    
    def _register_formatters(self) -> Dict[str, Type[OutputFormatter]]:
        """Register all available formatters."""
        formatters = {
            # Text formatters
            'text': TextFormatter,
            'txt': TextFormatter,
            'text-compact': lambda **kwargs: TextFormatter(column_separator=' ', max_column_width=30, min_column_width=5, indent_size=1, list_bullet='- ', **kwargs),
            'text-verbose': lambda **kwargs: TextFormatter(column_separator='  |  ', max_column_width=80, min_column_width=12, show_row_numbers=True, indent_size=4, **kwargs),
            
            # JSON formatters
            'json': JSONFormatter,
            'json-compact': lambda **kwargs: JSONFormatter(compact=True, sort_keys=True, **kwargs),
            'json-pretty': lambda **kwargs: JSONFormatter(indent=4, sort_keys=True, separators=(', ', ': '), **kwargs),
            'jsonl': JSONLinesFormatter,
            'json-lines': JSONLinesFormatter,
            
            # CSV formatters
            'csv': CSVFormatter,
            'tsv': TSVFormatter,
            'csv-excel': ExcelCSVFormatter,
            'psv': PipeDelimitedFormatter,
            
            # XML formatters
            'xml': XMLFormatter,
            'xml-compact': CompactXMLFormatter,
            'xml-attributes': AttributeXMLFormatter,
            
            # HTML formatters
            'html': HTMLFormatter,
            'html-minimal': MinimalHTMLFormatter,
            'html-bootstrap': BootstrapHTMLFormatter,
            
            # Markdown formatters
            'markdown': MarkdownFormatter,
            'md': MarkdownFormatter,
            'markdown-github': GitHubMarkdownFormatter,
            'markdown-simple': SimpleMarkdownFormatter,
            
            # YAML formatters
            'yaml': DefaultYAMLFormatter,
            'yml': DefaultYAMLFormatter,
        }
        
        # Add YAML variants if available
        if HAS_YAML:
            formatters.update({
                'yaml-compact': CompactYAMLFormatter,
                'yaml-verbose': VerboseYAMLFormatter,
            })
        
        return formatters
    
    def get_available_formats(self) -> List[str]:
        """Get list of all available format names."""
        return list(self._formatters.keys())
    
    def get_formatter(self, format_name: str, **config) -> OutputFormatter:
        """
        Get a formatter instance by name.
        
        Args:
            format_name: Name of the format (e.g., 'json', 'csv', 'html')
            **config: Configuration options to pass to the formatter
            
        Returns:
            OutputFormatter: Configured formatter instance
            
        Raises:
            ValueError: If format_name is not recognized
        """
        format_name = format_name.lower()
        
        if format_name not in self._formatters:
            available = ', '.join(sorted(self._formatters.keys()))
            raise ValueError(f"Unknown format '{format_name}'. Available formats: {available}")
        
        formatter_class = self._formatters[format_name]
        return formatter_class(**config)
    

    
    def detect_format_from_extension(self, filepath: str) -> str:
        """
        Detect format from file extension.
        
        Args:
            filepath: File path to analyze
            
        Returns:
            str: Detected format name
        """
        extension = os.path.splitext(filepath)[1].lower().lstrip('.')
        
        extension_map = {
            'txt': 'text',
            'json': 'json',
            'csv': 'csv',
            'tsv': 'tsv',
            'xml': 'xml',
            'html': 'html',
            'htm': 'html',
            'md': 'markdown',
            'markdown': 'markdown',
            'yaml': 'yaml',
            'yml': 'yaml',
            'jsonl': 'jsonl',
            'psv': 'psv',
        }
        
        return extension_map.get(extension, self._default_format)
    
    def get_content_type(self, format_name: str) -> str:
        """
        Get the MIME content type for a format.
        
        Args:
            format_name: Format name
            
        Returns:
            str: MIME content type
        """
        formatter = self.get_formatter(format_name)
        return formatter.get_content_type()
    
    def get_file_extension(self, format_name: str) -> str:
        """
        Get the recommended file extension for a format.
        
        Args:
            format_name: Format name
            
        Returns:
            str: File extension (without dot)
        """
        formatter = self.get_formatter(format_name)
        return formatter.get_file_extension()
    

    

    

    






# Global instance for formatter registry
output_manager = OutputManager()

# Convenience functions for accessing the manager
def get_available_formats() -> List[str]:
    """Get available formats from the global output manager."""
    return output_manager.get_available_formats()

def get_formatter(format_name: str, **config) -> OutputFormatter:
    """Get a formatter from the global output manager."""
    return output_manager.get_formatter(format_name, **config)