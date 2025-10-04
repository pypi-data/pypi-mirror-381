"""
HTML output formatter for scriptthing.

Provides HTML output with table formatting, styling, and responsive design.
"""

from typing import Any, Dict, List, Optional
from .base import TableFormatter, ConfigurableFormatter


class HTMLFormatter(TableFormatter, ConfigurableFormatter):
    """
    HTML formatter with table support and styling options.
    """
    
    DEFAULT_CONFIG = {
        'include_doctype': True,
        'include_html_wrapper': True,
        'include_head': True,
        'page_title': 'Script Output',
        'include_styling': True,
        'table_class': 'scriptthing-table',
        'responsive': True,
        'dark_mode': False,
        'bootstrap_css': False,
        'custom_css': '',
        'escape_html': True,
        'show_row_numbers': False,
        'striped_rows': True,
        'bordered_table': True,
        'compact_table': False,
        'sortable_table': False,
        'max_cell_length': 200,
        'truncate_cells': True,
    }
    
    def get_content_type(self) -> str:
        return 'text/html'
    
    def get_file_extension(self) -> str:
        return 'html'
    
    def format_table(self, data: List[Dict[str, Any]], headers: Optional[List[str]] = None) -> str:
        """
        Format tabular data as an HTML table.
        """
        if not data:
            return self._wrap_content("<p>No data to display.</p>")
        
        if headers is None:
            headers = list(data[0].keys())
        
        # Build table HTML
        table_html = []
        table_classes = [self.config['table_class']]
        
        if self.config['striped_rows']:
            table_classes.append('striped')
        if self.config['bordered_table']:
            table_classes.append('bordered')
        if self.config['compact_table']:
            table_classes.append('compact')
        if self.config['sortable_table']:
            table_classes.append('sortable')
        
        table_html.append(f'<table class="{" ".join(table_classes)}">')
        
        # Add row numbers column if requested
        if self.config['show_row_numbers']:
            headers = ['#'] + headers
        
        # Table header
        if self.show_headers:
            table_html.append('  <thead>')
            table_html.append('    <tr>')
            for header in headers:
                escaped_header = self._escape_html(str(header)) if self.config['escape_html'] else str(header)
                table_html.append(f'      <th>{escaped_header}</th>')
            table_html.append('    </tr>')
            table_html.append('  </thead>')
        
        # Table body
        table_html.append('  <tbody>')
        for i, row in enumerate(data):
            table_html.append('    <tr>')
            
            # Add row number if requested
            if self.config['show_row_numbers']:
                table_html.append(f'      <td class="row-number">{i + 1}</td>')
            
            # Add data cells
            for header in headers:
                if header == '#':
                    continue
                
                value = row.get(header, '')
                formatted_value = self._format_cell_value(value)
                escaped_value = self._escape_html(formatted_value) if self.config['escape_html'] else formatted_value
                table_html.append(f'      <td>{escaped_value}</td>')
            
            table_html.append('    </tr>')
        
        table_html.append('  </tbody>')
        table_html.append('</table>')
        
        return self._wrap_content('\n'.join(table_html))
    
    def _format_non_table_data(self, data: Any) -> str:
        """Format non-tabular data as HTML."""
        if isinstance(data, dict):
            return self._wrap_content(self._format_dict_as_html(data))
        elif isinstance(data, list):
            return self._wrap_content(self._format_list_as_html(data))
        else:
            escaped_data = self._escape_html(str(data)) if self.config['escape_html'] else str(data)
            return self._wrap_content(f'<p>{escaped_data}</p>')
    
    def _format_dict_as_html(self, data: Dict[str, Any], level: int = 0) -> str:
        """Format a dictionary as HTML definition list or nested structure."""
        if not data:
            return '<p><em>Empty dictionary</em></p>'
        
        # Handle special structures
        if 'title' in data and 'data' in data:
            title_html = f'<h{min(level + 2, 6)}>{self._escape_html(str(data["title"]))}</h{min(level + 2, 6)}>' if data['title'] else ''
            content_html = self._format_dict_as_html(data['data'], level + 1)
            return f'{title_html}\n{content_html}'
        
        if 'title' in data and 'items' in data:
            title_html = f'<h{min(level + 2, 6)}>{self._escape_html(str(data["title"]))}</h{min(level + 2, 6)}>' if data['title'] else ''
            content_html = self._format_list_as_html(data['items'], level + 1)
            return f'{title_html}\n{content_html}'
        
        # Regular dictionary as definition list
        html_parts = ['<dl>']
        
        for key, value in data.items():
            escaped_key = self._escape_html(str(key)) if self.config['escape_html'] else str(key)
            html_parts.append(f'  <dt>{escaped_key}</dt>')
            
            if isinstance(value, dict):
                html_parts.append(f'  <dd>{self._format_dict_as_html(value, level + 1)}</dd>')
            elif isinstance(value, list):
                html_parts.append(f'  <dd>{self._format_list_as_html(value, level + 1)}</dd>')
            else:
                escaped_value = self._escape_html(str(value)) if self.config['escape_html'] else str(value)
                html_parts.append(f'  <dd>{escaped_value}</dd>')
        
        html_parts.append('</dl>')
        return '\n'.join(html_parts)
    
    def _format_list_as_html(self, items: List[Any], level: int = 0) -> str:
        """Format a list as HTML unordered list."""
        if not items:
            return '<p><em>Empty list</em></p>'
        
        html_parts = ['<ul>']
        
        for item in items:
            if isinstance(item, dict):
                item_html = self._format_dict_as_html(item, level + 1)
                html_parts.append(f'  <li>{item_html}</li>')
            elif isinstance(item, list):
                item_html = self._format_list_as_html(item, level + 1)
                html_parts.append(f'  <li>{item_html}</li>')
            else:
                escaped_item = self._escape_html(str(item)) if self.config['escape_html'] else str(item)
                html_parts.append(f'  <li>{escaped_item}</li>')
        
        html_parts.append('</ul>')
        return '\n'.join(html_parts)
    
    def _format_cell_value(self, value: Any) -> str:
        """Format a single cell value."""
        if value is None:
            return '<em>null</em>'
        
        text = str(value)
        
        # Truncate if needed
        if self.config['truncate_cells'] and len(text) > self.config['max_cell_length']:
            text = text[:self.config['max_cell_length']] + '...'
        
        return text
    
    def _escape_html(self, text: str) -> str:
        """Escape HTML special characters."""
        return (text
                .replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace("'", '&#x27;'))
    
    def _wrap_content(self, content: str) -> str:
        """Wrap content in HTML document structure if configured."""
        if not self.config['include_html_wrapper']:
            return content
        
        html_parts = []
        
        if self.config['include_doctype']:
            html_parts.append('<!DOCTYPE html>')
        
        html_parts.append('<html lang="en">')
        
        if self.config['include_head']:
            html_parts.append('<head>')
            html_parts.append('  <meta charset="UTF-8">')
            html_parts.append('  <meta name="viewport" content="width=device-width, initial-scale=1.0">')
            html_parts.append(f'  <title>{self._escape_html(self.config["page_title"])}</title>')
            
            if self.config['bootstrap_css']:
                html_parts.append('  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">')
            
            if self.config['include_styling']:
                html_parts.append('  <style>')
                html_parts.append(self._get_default_css())
                if self.config['custom_css']:
                    html_parts.append(self.config['custom_css'])
                html_parts.append('  </style>')
            
            html_parts.append('</head>')
        
        html_parts.append('<body>')
        
        if self.config['bootstrap_css']:
            html_parts.append('<div class="container mt-4">')
            html_parts.append(content)
            html_parts.append('</div>')
        else:
            html_parts.append(content)
        
        if self.config['sortable_table']:
            html_parts.append(self._get_sortable_script())
        
        html_parts.append('</body>')
        html_parts.append('</html>')
        
        return '\n'.join(html_parts)
    
    def _get_default_css(self) -> str:
        """Get default CSS styling."""
        theme = 'dark' if self.config['dark_mode'] else 'light'
        
        css = f'''
    body {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        margin: 20px;
        line-height: 1.6;
        {'background-color: #1a1a1a; color: #e0e0e0;' if theme == 'dark' else 'background-color: #ffffff; color: #333333;'}
    }}
    
    .{self.config['table_class']} {{
        border-collapse: collapse;
        width: 100%;
        margin: 20px 0;
        {'background-color: #2a2a2a;' if theme == 'dark' else 'background-color: #ffffff;'}
    }}
    
    .{self.config['table_class']} th,
    .{self.config['table_class']} td {{
        padding: 8px 12px;
        text-align: left;
    }}
    
    .{self.config['table_class']} th {{
        {'background-color: #3a3a3a; color: #ffffff;' if theme == 'dark' else 'background-color: #f5f5f5; color: #333333;'}
        font-weight: 600;
    }}
    '''
        
        if self.config['bordered_table']:
            border_color = '#555555' if theme == 'dark' else '#dddddd'
            css += f'''
    .{self.config['table_class']}.bordered {{
        border: 1px solid {border_color};
    }}
    
    .{self.config['table_class']}.bordered th,
    .{self.config['table_class']}.bordered td {{
        border: 1px solid {border_color};
    }}
    '''
        
        if self.config['striped_rows']:
            stripe_color = '#333333' if theme == 'dark' else '#f9f9f9'
            css += f'''
    .{self.config['table_class']}.striped tbody tr:nth-child(even) {{
        background-color: {stripe_color};
    }}
    '''
        
        if self.config['compact_table']:
            css += f'''
    .{self.config['table_class']}.compact th,
    .{self.config['table_class']}.compact td {{
        padding: 4px 8px;
        font-size: 0.9em;
    }}
    '''
        
        if self.config['responsive']:
            css += f'''
    @media (max-width: 768px) {{
        .{self.config['table_class']} {{
            font-size: 0.8em;
        }}
        
        .{self.config['table_class']} th,
        .{self.config['table_class']} td {{
            padding: 4px 6px;
        }}
    }}
    '''
        
        css += '''
    .row-number {
        font-weight: bold;
        text-align: right;
    }
    
    dl {
        margin: 10px 0;
    }
    
    dt {
        font-weight: bold;
        margin-top: 10px;
    }
    
    dd {
        margin-left: 20px;
        margin-bottom: 5px;
    }
    
    ul {
        margin: 10px 0;
        padding-left: 20px;
    }
    
    em {
        font-style: italic;
        opacity: 0.7;
    }
    '''
        
        return css
    
    def _get_sortable_script(self) -> str:
        """Get JavaScript for sortable tables."""
        return f'''
<script>
document.addEventListener('DOMContentLoaded', function() {{
    const tables = document.querySelectorAll('.{self.config["table_class"]}.sortable');
    tables.forEach(table => {{
        const headers = table.querySelectorAll('thead th');
        headers.forEach((header, index) => {{
            header.style.cursor = 'pointer';
            header.addEventListener('click', () => sortTable(table, index));
        }});
    }});
}});

function sortTable(table, columnIndex) {{
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    
    const isNumeric = rows.every(row => {{
        const cell = row.cells[columnIndex];
        return cell && !isNaN(parseFloat(cell.textContent.trim()));
    }});
    
    rows.sort((a, b) => {{
        const aVal = a.cells[columnIndex].textContent.trim();
        const bVal = b.cells[columnIndex].textContent.trim();
        
        if (isNumeric) {{
            return parseFloat(aVal) - parseFloat(bVal);
        }} else {{
            return aVal.localeCompare(bVal);
        }}
    }});
    
    rows.forEach(row => tbody.appendChild(row));
}}
</script>
'''


class MinimalHTMLFormatter(HTMLFormatter):
    """
    Minimal HTML formatter without styling or wrapper.
    """
    
    DEFAULT_CONFIG = {
        **HTMLFormatter.DEFAULT_CONFIG,
        'include_doctype': False,
        'include_html_wrapper': False,
        'include_head': False,
        'include_styling': False,
        'bootstrap_css': False,
    }


class BootstrapHTMLFormatter(HTMLFormatter):
    """
    HTML formatter with Bootstrap styling.
    """
    
    DEFAULT_CONFIG = {
        **HTMLFormatter.DEFAULT_CONFIG,
        'bootstrap_css': True,
        'table_class': 'table table-striped table-bordered',
        'responsive': True,
    }