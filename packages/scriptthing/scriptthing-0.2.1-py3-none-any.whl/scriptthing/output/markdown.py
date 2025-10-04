"""
Markdown output formatter for scriptthing.

Provides Markdown output with table formatting, lists, and proper escaping.
"""

from typing import Any, Dict, List, Optional
import re
from .base import TableFormatter, ConfigurableFormatter


class MarkdownFormatter(TableFormatter, ConfigurableFormatter):
    """
    Markdown formatter with table and formatting support.
    """
    
    DEFAULT_CONFIG = {
        'table_format': 'github',  # 'github', 'simple', 'grid'
        'align_columns': True,
        'escape_pipes': True,
        'max_column_width': 50,
        'header_level': 2,  # Level for automatic headers (1-6)
        'use_code_blocks': True,
        'code_language': '',  # Default language for code blocks
        'list_style': 'dash',  # 'dash', 'asterisk', 'plus'
        'ordered_list': False,
        'indent_size': 2,
        'escape_markdown': True,
        'link_urls': True,  # Convert URLs to markdown links
        'emphasize_null': True,  # Emphasize null values
    }
    
    def get_content_type(self) -> str:
        return 'text/markdown'
    
    def get_file_extension(self) -> str:
        return 'md'
    
    def format_table(self, data: List[Dict[str, Any]], headers: Optional[List[str]] = None) -> str:
        """
        Format tabular data as a Markdown table.
        """
        if not data:
            return "_No data to display._\n"
        
        if headers is None:
            headers = list(data[0].keys())
        
        if self.config['table_format'] == 'github':
            return self._format_github_table(data, headers)
        elif self.config['table_format'] == 'simple':
            return self._format_simple_table(data, headers)
        elif self.config['table_format'] == 'grid':
            return self._format_grid_table(data, headers)
        else:
            return self._format_github_table(data, headers)
    
    def _format_github_table(self, data: List[Dict[str, Any]], headers: List[str]) -> str:
        """Format as GitHub-flavored Markdown table."""
        # Prepare data and calculate column widths
        formatted_data = []
        col_widths = {}
        
        # Initialize with header widths
        for header in headers:
            col_widths[header] = len(str(header))
        
        # Process data and calculate max widths
        for row in data:
            formatted_row = {}
            for header in headers:
                value = row.get(header, '')
                formatted_value = self._format_cell_value(value)
                formatted_row[header] = formatted_value
                
                if self.config['align_columns']:
                    col_widths[header] = max(col_widths[header], len(formatted_value))
            formatted_data.append(formatted_row)
        
        # Cap column widths if needed
        if self.config['max_column_width']:
            for header in headers:
                col_widths[header] = min(col_widths[header], self.config['max_column_width'])
        
        # Build table
        lines = []
        
        # Header row
        if self.show_headers:
            if self.config['align_columns']:
                header_row = '| ' + ' | '.join(
                    str(header).ljust(col_widths[header]) for header in headers
                ) + ' |'
            else:
                header_row = '| ' + ' | '.join(str(header) for header in headers) + ' |'
            lines.append(header_row)
            
            # Separator row
            if self.config['align_columns']:
                separator_row = '| ' + ' | '.join(
                    '-' * col_widths[header] for header in headers
                ) + ' |'
            else:
                separator_row = '| ' + ' | '.join('---' for _ in headers) + ' |'
            lines.append(separator_row)
        
        # Data rows
        for row in formatted_data:
            if self.config['align_columns']:
                data_row = '| ' + ' | '.join(
                    row.get(header, '').ljust(col_widths[header]) for header in headers
                ) + ' |'
            else:
                data_row = '| ' + ' | '.join(
                    row.get(header, '') for header in headers
                ) + ' |'
            lines.append(data_row)
        
        return '\n'.join(lines) + '\n'
    
    def _format_simple_table(self, data: List[Dict[str, Any]], headers: List[str]) -> str:
        """Format as simple text table without borders."""
        lines = []
        
        # Calculate column widths
        col_widths = {}
        for header in headers:
            col_widths[header] = len(str(header))
        
        for row in data:
            for header in headers:
                value = self._format_cell_value(row.get(header, ''))
                col_widths[header] = max(col_widths[header], len(value))
        
        # Header
        if self.show_headers:
            header_line = '  '.join(str(header).ljust(col_widths[header]) for header in headers)
            lines.append(header_line)
            separator_line = '  '.join('-' * col_widths[header] for header in headers)
            lines.append(separator_line)
        
        # Data
        for row in data:
            data_line = '  '.join(
                self._format_cell_value(row.get(header, '')).ljust(col_widths[header])
                for header in headers
            )
            lines.append(data_line)
        
        return '\n'.join(lines) + '\n'
    
    def _format_grid_table(self, data: List[Dict[str, Any]], headers: List[str]) -> str:
        """Format as grid table with borders."""
        # Calculate column widths
        col_widths = {}
        for header in headers:
            col_widths[header] = len(str(header))
        
        for row in data:
            for header in headers:
                value = self._format_cell_value(row.get(header, ''))
                col_widths[header] = max(col_widths[header], len(value))
        
        # Build horizontal separator
        separator = '+' + '+'.join('-' * (col_widths[header] + 2) for header in headers) + '+'
        
        lines = [separator]
        
        # Header
        if self.show_headers:
            header_line = '| ' + ' | '.join(
                str(header).ljust(col_widths[header]) for header in headers
            ) + ' |'
            lines.append(header_line)
            lines.append(separator)
        
        # Data
        for row in data:
            data_line = '| ' + ' | '.join(
                self._format_cell_value(row.get(header, '')).ljust(col_widths[header])
                for header in headers
            ) + ' |'
            lines.append(data_line)
        
        lines.append(separator)
        return '\n'.join(lines) + '\n'
    
    def _format_non_table_data(self, data: Any) -> str:
        """Format non-tabular data as Markdown."""
        if isinstance(data, dict):
            return self._format_dict_as_markdown(data)
        elif isinstance(data, list):
            return self._format_list_as_markdown(data)
        else:
            return self._format_scalar_as_markdown(data)
    
    def _format_dict_as_markdown(self, data: Dict[str, Any], level: int = 0) -> str:
        """Format dictionary as Markdown with headers and lists."""
        if not data:
            return "_Empty dictionary_\n"
        
        lines = []
        
        # Handle special structures
        if 'title' in data and 'data' in data:
            if data['title']:
                header_level = min(self.config['header_level'] + level, 6)
                lines.append(f"{'#' * header_level} {data['title']}\n")
            lines.append(self._format_dict_as_markdown(data['data'], level + 1))
            return '\n'.join(lines)
        
        if 'title' in data and 'items' in data:
            if data['title']:
                header_level = min(self.config['header_level'] + level, 6)
                lines.append(f"{'#' * header_level} {data['title']}\n")
            lines.append(self._format_list_as_markdown(data['items'], level))
            return '\n'.join(lines)
        
        # Regular dictionary
        for key, value in data.items():
            key_str = self._escape_markdown_text(str(key)) if self.config['escape_markdown'] else str(key)
            
            if isinstance(value, dict):
                if level == 0:
                    header_level = min(self.config['header_level'] + level, 6)
                    lines.append(f"{'#' * header_level} {key_str}\n")
                    lines.append(self._format_dict_as_markdown(value, level + 1))
                else:
                    lines.append(f"**{key_str}**\n")
                    lines.append(self._format_dict_as_markdown(value, level + 1))
            elif isinstance(value, list):
                lines.append(f"**{key_str}**\n")
                lines.append(self._format_list_as_markdown(value, level))
            else:
                value_str = self._format_scalar_as_markdown(value)
                lines.append(f"**{key_str}**: {value_str}")
        
        return '\n'.join(lines) + '\n'
    
    def _format_list_as_markdown(self, items: List[Any], level: int = 0) -> str:
        """Format list as Markdown list."""
        if not items:
            return "_Empty list_\n"
        
        lines = []
        indent = ' ' * (level * self.config['indent_size'])
        
        for i, item in enumerate(items):
            if self.config['ordered_list']:
                bullet = f"{i + 1}. "
            else:
                bullet_char = {
                    'dash': '-',
                    'asterisk': '*',
                    'plus': '+'
                }.get(self.config['list_style'], '-')
                bullet = f"{bullet_char} "
            
            if isinstance(item, dict):
                lines.append(f"{indent}{bullet}Complex item:")
                item_content = self._format_dict_as_markdown(item, level + 1)
                # Indent the content
                indented_content = '\n'.join(
                    ' ' * self.config['indent_size'] + line if line.strip() else line
                    for line in item_content.split('\n')
                )
                lines.append(indented_content)
            elif isinstance(item, list):
                lines.append(f"{indent}{bullet}Nested list:")
                nested_content = self._format_list_as_markdown(item, level + 1)
                lines.append(nested_content)
            else:
                item_str = self._format_scalar_as_markdown(item)
                lines.append(f"{indent}{bullet}{item_str}")
        
        return '\n'.join(lines) + '\n'
    
    def _format_scalar_as_markdown(self, value: Any) -> str:
        """Format a scalar value for Markdown."""
        if value is None:
            return "_null_" if self.config['emphasize_null'] else "null"
        
        elif isinstance(value, bool):
            return f"**{value}**"
        
        elif isinstance(value, (int, float)):
            return f"`{value}`"
        
        elif isinstance(value, str):
            # Handle URLs
            if self.config['link_urls'] and self._is_url(value):
                return f"[{value}]({value})"
            
            # Handle code-like strings
            if self.config['use_code_blocks'] and ('\n' in value or len(value) > 100):
                lang = self.config['code_language']
                return f"```{lang}\n{value}\n```"
            
            # Escape markdown if needed
            if self.config['escape_markdown']:
                return self._escape_markdown_text(value)
            else:
                return value
        
        else:
            return str(value)
    
    def _format_cell_value(self, value: Any) -> str:
        """Format a table cell value."""
        if value is None:
            return "_null_" if self.config['emphasize_null'] else "null"
        
        text = str(value)
        
        # Escape pipes for table formatting
        if self.config['escape_pipes']:
            text = text.replace('|', '\\|')
        
        # Escape other markdown characters in table cells
        if self.config['escape_markdown']:
            text = self._escape_markdown_text(text, in_table=True)
        
        # Truncate if needed
        if self.config['max_column_width'] and len(text) > self.config['max_column_width']:
            text = text[:self.config['max_column_width'] - 3] + '...'
        
        return text
    
    def _escape_markdown_text(self, text: str, in_table: bool = False) -> str:
        """Escape Markdown special characters."""
        # Characters that need escaping in Markdown
        chars_to_escape = ['\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '#', '+', '-', '.', '!']
        
        if in_table:
            chars_to_escape.append('|')
        
        for char in chars_to_escape:
            text = text.replace(char, f'\\{char}')
        
        return text
    
    def _is_url(self, text: str) -> bool:
        """Check if text looks like a URL."""
        url_pattern = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return bool(url_pattern.match(text))


class GitHubMarkdownFormatter(MarkdownFormatter):
    """
    Markdown formatter optimized for GitHub.
    """
    
    DEFAULT_CONFIG = {
        **MarkdownFormatter.DEFAULT_CONFIG,
        'table_format': 'github',
        'use_code_blocks': True,
        'link_urls': True,
        'escape_markdown': True,
    }


class SimpleMarkdownFormatter(MarkdownFormatter):
    """
    Simple Markdown formatter without fancy features.
    """
    
    DEFAULT_CONFIG = {
        **MarkdownFormatter.DEFAULT_CONFIG,
        'table_format': 'simple',
        'align_columns': False,
        'use_code_blocks': False,
        'link_urls': False,
        'escape_markdown': False,
    }


class WikiMarkdownFormatter(MarkdownFormatter):
    """
    Markdown formatter for wiki-style documentation.
    """
    
    DEFAULT_CONFIG = {
        **MarkdownFormatter.DEFAULT_CONFIG,
        'table_format': 'grid',
        'header_level': 1,
        'use_code_blocks': True,
        'code_language': 'text',
        'ordered_list': True,
    }