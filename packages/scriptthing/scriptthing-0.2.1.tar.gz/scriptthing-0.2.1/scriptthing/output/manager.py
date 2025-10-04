"""
Simple output manager for scriptthing.
"""

from typing import Dict, List
import os

from .base import OutputFormatter
from .text import TextFormatter
from .json_formatter import JSONFormatter
from .csv import CSVFormatter


class OutputManager:
    """Simple formatter registry."""
    
    def __init__(self):
        self._formatters = {
            'text': TextFormatter,
            'json': JSONFormatter, 
            'csv': CSVFormatter,
        }
    
    def get_formatter(self, format_name: str, **config) -> OutputFormatter:
        """Get formatter instance."""
        if format_name not in self._formatters:
            raise ValueError(f"Unknown format: {format_name}")
        return self._formatters[format_name](**config)


# Global instance
output_manager = OutputManager()

def get_formatter(format_name: str, **config) -> OutputFormatter:
    """Get formatter from global manager."""
    return output_manager.get_formatter(format_name, **config)
    return output_manager.get_formatter(format_name, **config)