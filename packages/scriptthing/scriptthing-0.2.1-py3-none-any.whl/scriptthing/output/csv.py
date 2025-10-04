"""
CSV output formatter for scriptthing.
"""

import csv
from io import StringIO
from typing import Any, Dict, List, Optional
from .base import OutputFormatter


class CSVFormatter(OutputFormatter):
    """CSV formatter with configurable options."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.delimiter = kwargs.get('delimiter', ',')
        self.include_headers = kwargs.get('include_headers', True)
        self.quoting = kwargs.get('quoting', csv.QUOTE_MINIMAL)
    
    def get_content_type(self) -> str:
        return 'text/csv'
    
    def get_file_extension(self) -> str:
        return 'csv'
    
    def format_data(self, data: Any) -> str:
        """Format data as CSV."""
        if isinstance(data, list) and data and isinstance(data[0], dict):
            return self._format_table(data)
        elif isinstance(data, dict):
            return self._format_table([{'key': k, 'value': v} for k, v in data.items()])
        elif isinstance(data, list):
            return self._format_table([{'item': item} for item in data])
        else:
            return str(data)
    
    def _format_table(self, data: List[Dict[str, Any]]) -> str:
        """Format table data as CSV."""
        if not data:
            return ""
        
        output = StringIO()
        headers = list(data[0].keys())
        writer = csv.writer(output, delimiter=self.delimiter, quoting=self.quoting)
        
        if self.include_headers:
            writer.writerow(headers)
        
        for row in data:
            writer.writerow([str(row.get(h, '')) for h in headers])
        
        return output.getvalue()
    


# Aliases for backwards compatibility
TSVFormatter = lambda **kwargs: CSVFormatter(delimiter='\t', **kwargs)
ExcelCSVFormatter = lambda **kwargs: CSVFormatter(quoting=csv.QUOTE_ALL, **kwargs)
PipeDelimitedFormatter = lambda **kwargs: CSVFormatter(delimiter='|', **kwargs)
CustomDelimiterCSVFormatter = CSVFormatter
