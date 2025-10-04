"""
CSV output formatter for scriptthing.

Provides CSV output with configurable delimiters, quoting, and formatting options.
"""

import csv
from io import StringIO
from typing import Any, Dict, List, Optional
from .base import TableFormatter, ConfigurableFormatter


class CSVFormatter(TableFormatter, ConfigurableFormatter):
    """
    CSV formatter with extensive configuration options.
    """
    
    DEFAULT_CONFIG = {
        'delimiter': ',',
        'quotechar': '"',
        'quoting': csv.QUOTE_MINIMAL,
        'lineterminator': '\n',
        'escapechar': None,
        'doublequote': True,
        'skipinitialspace': False,
        'include_headers': True,
        'header_prefix': '',
        'header_suffix': '',
        'null_value': '',
        'boolean_format': 'string',  # 'string', 'numeric', 'yes_no'
        'date_format': '%Y-%m-%d',
        'datetime_format': '%Y-%m-%d %H:%M:%S',
        'float_precision': None,  # None for default, or number of decimal places
    }
    
    def get_content_type(self) -> str:
        return 'text/csv'
    
    def get_file_extension(self) -> str:
        return 'csv'
    
    def format_table(self, data: List[Dict[str, Any]], headers: Optional[List[str]] = None) -> str:
        """
        Format tabular data as CSV.
        """
        if not data:
            return ""
        
        if headers is None:
            headers = list(data[0].keys())
        
        output = StringIO()
        
        # Create CSV writer with configured options
        writer = self._create_csv_writer(output)
        
        # Write headers if requested
        if self.config['include_headers']:
            formatted_headers = [
                f"{self.config['header_prefix']}{header}{self.config['header_suffix']}"
                for header in headers
            ]
            writer.writerow(formatted_headers)
        
        # Write data rows
        for row in data:
            formatted_row = []
            for header in headers:
                value = row.get(header, '')
                formatted_value = self._format_value(value)
                formatted_row.append(formatted_value)
            writer.writerow(formatted_row)
        
        return output.getvalue()
    
    def _format_non_table_data(self, data: Any) -> str:
        """Format non-tabular data by converting to table format."""
        if isinstance(data, dict):
            # Convert dictionary to two-column table
            table_data = [
                {'key': str(key), 'value': value}
                for key, value in data.items()
            ]
            return self.format_table(table_data, ['key', 'value'])
        
        elif isinstance(data, list):
            # Convert list to single-column table
            table_data = [
                {'item': item}
                for item in data
            ]
            return self.format_table(table_data, ['item'])
        
        else:
            # Single value - create single cell table
            table_data = [{'value': data}]
            return self.format_table(table_data, ['value'])
    
    def _create_csv_writer(self, output: StringIO) -> csv.writer:
        """Create a CSV writer with configured options."""
        dialect_kwargs = {
            'delimiter': self.config['delimiter'],
            'quotechar': self.config['quotechar'],
            'quoting': self.config['quoting'],
            'lineterminator': self.config['lineterminator'],
            'doublequote': self.config['doublequote'],
            'skipinitialspace': self.config['skipinitialspace'],
        }
        
        if self.config['escapechar'] is not None:
            dialect_kwargs['escapechar'] = self.config['escapechar']
        
        return csv.writer(output, **dialect_kwargs)
    
    def _format_value(self, value: Any) -> str:
        """Format a single value for CSV output."""
        if value is None:
            return self.config['null_value']
        
        elif isinstance(value, bool):
            if self.config['boolean_format'] == 'numeric':
                return '1' if value else '0'
            elif self.config['boolean_format'] == 'yes_no':
                return 'Yes' if value else 'No'
            else:  # string
                return 'True' if value else 'False'
        
        elif isinstance(value, float):
            if self.config['float_precision'] is not None:
                return f"{value:.{self.config['float_precision']}f}"
            else:
                return str(value)
        
        elif hasattr(value, 'strftime'):  # datetime-like objects
            try:
                if hasattr(value, 'time'):  # datetime
                    return value.strftime(self.config['datetime_format'])
                else:  # date
                    return value.strftime(self.config['date_format'])
            except (AttributeError, ValueError):
                return str(value)
        
        else:
            return str(value)
    



class TSVFormatter(CSVFormatter):
    """
    Tab-separated values formatter.
    """
    
    DEFAULT_CONFIG = {
        **CSVFormatter.DEFAULT_CONFIG,
        'delimiter': '\t',
        'quoting': csv.QUOTE_NONE,
        'escapechar': '\\',
    }
    
    def get_content_type(self) -> str:
        return 'text/tab-separated-values'
    
    def get_file_extension(self) -> str:
        return 'tsv'


class ExcelCSVFormatter(CSVFormatter):
    """
    CSV formatter optimized for Excel compatibility.
    """
    
    DEFAULT_CONFIG = {
        **CSVFormatter.DEFAULT_CONFIG,
        'quoting': csv.QUOTE_ALL,
        'lineterminator': '\r\n',
        'boolean_format': 'yes_no',
        'date_format': '%m/%d/%Y',
        'datetime_format': '%m/%d/%Y %I:%M:%S %p',
        'float_precision': 2,
    }


class PipeDelimitedFormatter(CSVFormatter):
    """
    Pipe-delimited formatter for data that might contain commas.
    """
    
    DEFAULT_CONFIG = {
        **CSVFormatter.DEFAULT_CONFIG,
        'delimiter': '|',
        'quoting': csv.QUOTE_MINIMAL,
    }
    
    def get_file_extension(self) -> str:
        return 'psv'  # Pipe-separated values


class CustomDelimiterCSVFormatter(CSVFormatter):
    """
    CSV formatter that allows easy customization of delimiter.
    """
    
    def __init__(self, delimiter: str = ',', **kwargs):
        kwargs['delimiter'] = delimiter
        super().__init__(**kwargs)


# Utility functions for CSV operations

def detect_csv_dialect(sample_text: str) -> csv.Dialect:
    """
    Attempt to detect the CSV dialect from a sample of text.
    
    Args:
        sample_text: A sample of CSV text to analyze
        
    Returns:
        csv.Dialect: The detected dialect
    """
    sniffer = csv.Sniffer()
    try:
        return sniffer.sniff(sample_text)
    except csv.Error:
        # Fall back to default dialect
        return csv.excel


def escape_csv_value(value: str, delimiter: str = ',') -> str:
    """
    Manually escape a value for CSV if needed.
    
    Args:
        value: The value to escape
        delimiter: The CSV delimiter being used
        
    Returns:
        str: The escaped value
    """
    if delimiter in value or '"' in value or '\n' in value:
        # Need to quote and escape
        escaped = value.replace('"', '""')
        return f'"{escaped}"'
    return value