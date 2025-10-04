"""
Simple output formatting utilities for scriptthing.

Basic usage:
    from scriptthing.output import from_dict, Output
    
    data = from_dict({'name': 'John', 'age': 30})
    json_output = data.as_json()
    csv_output = data.as_csv()
"""

# Core classes and functions
from .base import OutputFormatter, sanitize_filename, truncate_string
from .text import TextFormatter  
from .json_formatter import JSONFormatter, JSONLinesFormatter
from .csv import CSVFormatter, TSVFormatter, ExcelCSVFormatter, PipeDelimitedFormatter, CustomDelimiterCSVFormatter
from .manager import get_formatter
from .core import (
    Output,
    from_dict,
    from_list, 
    from_table,
    from_json,
    from_csv,
    from_any,
    empty
)


__all__ = [
    'OutputFormatter',
    'TextFormatter', 
    'JSONFormatter',
    'JSONLinesFormatter',
    'CSVFormatter',
    'TSVFormatter',
    'ExcelCSVFormatter',
    'PipeDelimitedFormatter', 
    'CustomDelimiterCSVFormatter',
    'get_formatter',
    'Output',
    'from_dict',
    'from_list',
    'from_table', 
    'from_json',
    'from_csv',
    'from_any',
    'empty',
    'sanitize_filename',
    'truncate_string',
]
