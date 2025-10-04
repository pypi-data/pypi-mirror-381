"""
Plain text output formatter for scriptthing.

Provides clean, readable text output with proper alignment and formatting
for tables, lists, and key-value pairs.
"""

from typing import Any, Dict, List, Optional
from .base import TableFormatter, ConfigurableFormatter


class TextFormatter(TableFormatter, ConfigurableFormatter):
    """
    Plain text formatter with table formatting capabilities.
    """
    
    DEFAULT_CONFIG = {
        'column_separator': ' | ',
        'header_separator': '-',
        'max_column_width': 50,
        'min_column_width': 8,
        'show_row_numbers': False,
        'align_numbers_right': True,
        'truncate_long_values': True,
        'indent_size': 2,
        'list_bullet': '• ',
        'numbered_list': False,
    }
    
    def get_content_type(self) -> str:
        return 'text/plain'
    
    def get_file_extension(self) -> str:
        return 'txt'
    
    def format_table(self, data: List[Dict[str, Any]], headers: Optional[List[str]] = None) -> str:
        """
        Format tabular data as a well-aligned text table.
        """
        if not data:
            return "No data to display."
        
        if headers is None:
            headers = list(data[0].keys())
        
        # Convert all values to strings and calculate column widths
        str_data = []
        col_widths = {}
        
        # Initialize column widths with header lengths
        for header in headers:
            col_widths[header] = max(len(str(header)), self.config['min_column_width'])
        
        # Process data and calculate max widths
        for row in data:
            str_row = {}
            for header in headers:
                value = row.get(header, '')
                str_value = str(value)
                
                # Truncate if needed
                if self.config['truncate_long_values'] and len(str_value) > self.config['max_column_width']:
                    from .base import truncate_string
                    str_value = truncate_string(str_value, self.config['max_column_width'])
                
                str_row[header] = str_value
                col_widths[header] = max(col_widths[header], len(str_value))
            str_data.append(str_row)
        
        # Cap column widths
        for header in headers:
            col_widths[header] = min(col_widths[header], self.config['max_column_width'])
        
        # Build the table
        lines = []
        separator = self.config['column_separator']
        
        # Add row numbers column if requested
        if self.config['show_row_numbers']:
            row_num_width = len(str(len(data)))
            headers = ['#'] + headers
            col_widths['#'] = max(row_num_width, 1)
        
        # Header row
        if self.show_headers:
            header_line = separator.join(
                self._align_text(str(header), col_widths[header], header)
                for header in headers
            )
            lines.append(header_line)
            
            # Header separator line
            sep_line = separator.join(
                self.config['header_separator'] * col_widths[header]
                for header in headers
            )
            lines.append(sep_line)
        
        # Data rows
        for i, row in enumerate(str_data):
            row_parts = []
            
            if self.config['show_row_numbers']:
                row_parts.append(self._align_text(str(i + 1), col_widths['#'], '#'))
            
            for header in headers:
                if header == '#':
                    continue
                value = row.get(header, '')
                aligned_value = self._align_text(value, col_widths[header], header)
                row_parts.append(aligned_value)
            
            lines.append(separator.join(row_parts))
        
        return '\n'.join(lines)
    
    def _format_non_table_data(self, data: Any) -> str:
        """Format non-tabular data as readable text."""
        if isinstance(data, dict):
            return self._format_dict(data)
        elif isinstance(data, list):
            return self._format_list(data)
        else:
            return str(data)
    
    def _format_dict(self, data: Dict[str, Any], indent: int = 0) -> str:
        """Format a dictionary as key-value pairs."""
        if not data:
            return "{}"
        
        lines = []
        indent_str = ' ' * (indent * self.config['indent_size'])
        
        # Handle special structures
        if 'title' in data and 'data' in data:
            # Key-value data with title
            if data['title']:
                lines.append(f"{indent_str}{data['title']}:")
                indent += 1
                indent_str = ' ' * (indent * self.config['indent_size'])
            return self._format_dict(data['data'], indent)
        
        if 'title' in data and 'items' in data:
            # List data with title
            if data['title']:
                lines.append(f"{indent_str}{data['title']}:")
            return self._format_list(data['items'], indent + (1 if data['title'] else 0))
        
        # Regular dictionary
        max_key_length = max(len(str(key)) for key in data.keys()) if data else 0
        
        for key, value in data.items():
            key_str = str(key).ljust(max_key_length)
            
            if isinstance(value, (dict, list)) and value:
                lines.append(f"{indent_str}{key_str}:")
                if isinstance(value, dict):
                    lines.append(self._format_dict(value, indent + 1))
                else:
                    lines.append(self._format_list(value, indent + 1))
            else:
                lines.append(f"{indent_str}{key_str}: {value}")
        
        return '\n'.join(lines)
    
    def _format_list(self, items: List[Any], indent: int = 0) -> str:
        """Format a list as bulleted or numbered items."""
        if not items:
            return "[]"
        
        lines = []
        indent_str = ' ' * (indent * self.config['indent_size'])
        
        for i, item in enumerate(items):
            if self.config['numbered_list']:
                bullet = f"{i + 1}. "
            else:
                bullet = self.config['list_bullet']
            
            if isinstance(item, (dict, list)) and item:
                lines.append(f"{indent_str}{bullet}(complex item)")
                if isinstance(item, dict):
                    lines.append(self._format_dict(item, indent + 1))
                else:
                    lines.append(self._format_list(item, indent + 1))
            else:
                lines.append(f"{indent_str}{bullet}{item}")
        
        return '\n'.join(lines)
    
    def _align_text(self, text: str, width: int, column_name: str) -> str:
        """Align text within a column based on content type."""
        text = str(text)
        
        # Right-align numbers if configured
        if (self.config['align_numbers_right'] and 
            column_name != '#' and 
            self._is_numeric(text)):
            return text.rjust(width)
        else:
            return text.ljust(width)
    
    def _is_numeric(self, text: str) -> bool:
        """Check if text represents a number."""
        try:
            float(text)
            return True
        except (ValueError, TypeError):
            return False


