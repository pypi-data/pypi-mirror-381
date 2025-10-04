"""
Core Output class for scriptthing.output package.

Provides an intermediate representation that hides input formats and
offers a unified interface for output rendering and data transformation.
"""

from typing import Any, Dict, List, Optional, Callable, Union, Iterator
from copy import deepcopy
import json
import csv
from io import StringIO
from datetime import datetime

from .manager import output_manager


class Output:
    """
    Intermediate representation for data that can be rendered in multiple formats.
    
    This class provides a format-agnostic interface for data manipulation and
    final output rendering. Data transformations return new Output objects,
    allowing for chaining operations.
    """
    
    def __init__(self, data: Any, metadata: Optional[Dict[str, Any]] = None, data_type: str = 'auto'):
        """
        Initialize Output with data and optional metadata.
        
        Args:
            data: The actual data (dict, list, primitive, etc.)
            metadata: Optional metadata about the data
            data_type: Hint about data structure ('table', 'object', 'list', 'auto')
        """
        self._data = data
        self._metadata = metadata or {}
        self._data_type = data_type
        
        # Auto-detect data type if not specified
        if data_type == 'auto':
            self._data_type = self._detect_data_type(data)
    
    def _detect_data_type(self, data: Any) -> str:
        """Automatically detect the type of data structure."""
        if isinstance(data, list) and data and isinstance(data[0], dict):
            # List of dictionaries = table
            return 'table'
        elif isinstance(data, list):
            return 'list'
        elif isinstance(data, dict):
            return 'object'
        else:
            return 'scalar'
    
    @property
    def data(self) -> Any:
        """Get the underlying data (read-only access)."""
        return self._data
    
    @property
    def metadata(self) -> Dict[str, Any]:
        """Get metadata dictionary."""
        return self._metadata.copy()
    
    @property
    def data_type(self) -> str:
        """Get the detected data type."""
        return self._data_type
    
    # === Transformation Methods (return new Output objects) ===
    
    def filter(self, predicate: Callable[[Any], bool]) -> 'Output':
        """
        Filter data based on predicate function.
        
        Args:
            predicate: Function that returns True for items to keep
            
        Returns:
            Output: New Output object with filtered data
        """
        if self._data_type == 'table' and isinstance(self._data, list):
            filtered_data = [item for item in self._data if predicate(item)]
            return Output(filtered_data, self._metadata, 'table')
        elif self._data_type == 'list' and isinstance(self._data, list):
            filtered_data = [item for item in self._data if predicate(item)]
            return Output(filtered_data, self._metadata, 'list')
        else:
            # For non-list data, apply predicate to the data itself
            if predicate(self._data):
                return Output(self._data, self._metadata, self._data_type)
            else:
                return Output(None, self._metadata, 'scalar')
    
    def map(self, transformer: Callable[[Any], Any]) -> 'Output':
        """
        Transform each item in the data.
        
        Args:
            transformer: Function to transform each item
            
        Returns:
            Output: New Output object with transformed data
        """
        if self._data_type in ['table', 'list'] and isinstance(self._data, list):
            transformed_data = [transformer(item) for item in self._data]
            return Output(transformed_data, self._metadata, self._data_type)
        else:
            # For non-list data, apply transformer to the data itself
            transformed_data = transformer(self._data)
            return Output(transformed_data, self._metadata, self._detect_data_type(transformed_data))
    
    def sort(self, key: Union[str, Callable[[Any], Any]] = None, reverse: bool = False) -> 'Output':
        """
        Sort the data.
        
        Args:
            key: Sort key (string for dict key, function for custom sorting)
            reverse: Sort in reverse order
            
        Returns:
            Output: New Output object with sorted data
        """
        if not isinstance(self._data, list):
            return Output(self._data, self._metadata, self._data_type)
        
        if isinstance(key, str):
            # Sort by dictionary key
            sorted_data = sorted(self._data, 
                               key=lambda x: x.get(key, '') if isinstance(x, dict) else str(x),
                               reverse=reverse)
        elif callable(key):
            # Sort by custom function
            sorted_data = sorted(self._data, key=key, reverse=reverse)
        else:
            # Default sort
            sorted_data = sorted(self._data, reverse=reverse)
        
        return Output(sorted_data, self._metadata, self._data_type)
    
    def limit(self, count: int, offset: int = 0) -> 'Output':
        """
        Limit the number of items.
        
        Args:
            count: Maximum number of items to include
            offset: Number of items to skip from the beginning
            
        Returns:
            Output: New Output object with limited data
        """
        if isinstance(self._data, list):
            limited_data = self._data[offset:offset + count]
            return Output(limited_data, self._metadata, self._data_type)
        else:
            return Output(self._data, self._metadata, self._data_type)
    
    def select(self, *columns: str) -> 'Output':
        """
        Select specific columns from table data.
        
        Args:
            columns: Column names to select
            
        Returns:
            Output: New Output object with selected columns
        """
        if self._data_type == 'table' and isinstance(self._data, list):
            selected_data = []
            for row in self._data:
                if isinstance(row, dict):
                    selected_row = {col: row.get(col) for col in columns}
                    selected_data.append(selected_row)
            return Output(selected_data, self._metadata, 'table')
        else:
            return Output(self._data, self._metadata, self._data_type)
    
    def group_by(self, key: str) -> 'Output':
        """
        Group table data by a column value.
        
        Args:
            key: Column name to group by
            
        Returns:
            Output: New Output object with grouped data
        """
        if self._data_type == 'table' and isinstance(self._data, list):
            groups = {}
            for row in self._data:
                if isinstance(row, dict):
                    group_key = row.get(key, 'unknown')
                    if group_key not in groups:
                        groups[group_key] = []
                    groups[group_key].append(row)
            
            return Output(groups, self._metadata, 'object')
        else:
            return Output(self._data, self._metadata, self._data_type)
    
    def add_metadata(self, **kwargs) -> 'Output':
        """
        Add metadata to the Output object.
        
        Returns:
            Output: New Output object with additional metadata
        """
        new_metadata = {**self._metadata, **kwargs}
        return Output(self._data, new_metadata, self._data_type)
    
    # === Output Rendering Methods ===
    
    def as_json(self, **kwargs) -> str:
        """Render as JSON format."""
        formatter = output_manager.get_formatter('json', **kwargs)
        return formatter.format_data(self._data)
    
    def as_json_pretty(self, **kwargs) -> str:
        """Render as pretty-printed JSON."""
        formatter = output_manager.get_formatter('json-pretty', **kwargs)
        return formatter.format_data(self._data)
    
    def as_json_compact(self, **kwargs) -> str:
        """Render as compact JSON."""
        formatter = output_manager.get_formatter('json-compact', **kwargs)
        return formatter.format_data(self._data)
    
    def as_csv(self, **kwargs) -> str:
        """Render as CSV format."""
        formatter = output_manager.get_formatter('csv', **kwargs)
        if self._data_type == 'table':
            return formatter.format_table(self._data)
        else:
            return formatter.format_data(self._data)
    
    def as_tsv(self, **kwargs) -> str:
        """Render as TSV format."""
        formatter = output_manager.get_formatter('tsv', **kwargs)
        if self._data_type == 'table':
            return formatter.format_table(self._data)
        else:
            return formatter.format_data(self._data)
    
    def as_html(self, **kwargs) -> str:
        """Render as HTML format."""
        formatter = output_manager.get_formatter('html', **kwargs)
        if self._data_type == 'table':
            return formatter.format_table(self._data)
        else:
            return formatter.format_data(self._data)
    
    def as_html_table(self, **kwargs) -> str:
        """Render as HTML table (minimal HTML)."""
        formatter = output_manager.get_formatter('html-minimal', **kwargs)
        if self._data_type == 'table':
            return formatter.format_table(self._data)
        else:
            return formatter.format_data(self._data)
    
    def as_markdown(self, **kwargs) -> str:
        """Render as Markdown format."""
        formatter = output_manager.get_formatter('markdown', **kwargs)
        if self._data_type == 'table':
            return formatter.format_table(self._data)
        else:
            return formatter.format_data(self._data)
    
    def as_xml(self, **kwargs) -> str:
        """Render as XML format."""
        formatter = output_manager.get_formatter('xml', **kwargs)
        return formatter.format_data(self._data)
    
    def as_yaml(self, **kwargs) -> str:
        """Render as YAML format."""
        formatter = output_manager.get_formatter('yaml', **kwargs)
        return formatter.format_data(self._data)
    
    def as_text(self, **kwargs) -> str:
        """Render as formatted text."""
        formatter = output_manager.get_formatter('text', **kwargs)
        if self._data_type == 'table':
            return formatter.format_table(self._data)
        else:
            return formatter.format_data(self._data)
    
    def as_format(self, format_name: str, **kwargs) -> str:
        """
        Render using any available format.
        
        Args:
            format_name: Name of the format to use
            **kwargs: Format-specific configuration
            
        Returns:
            str: Formatted output
        """
        formatter = output_manager.get_formatter(format_name, **kwargs)
        if self._data_type == 'table' and format_name in ['csv', 'tsv', 'html', 'markdown', 'text']:
            return formatter.format_table(self._data)
        else:
            return formatter.format_data(self._data)
    
    def save_to(self, filepath: str, format_name: str = None, **kwargs) -> None:
        """
        Save output to file.
        
        Args:
            filepath: Path to save file
            format_name: Format to use (auto-detected if None)
            **kwargs: Format-specific configuration
        """
        import os
        
        if format_name is None:
            format_name = output_manager.detect_format_from_extension(filepath)
        
        # Generate the output content
        formatted_output = self.as_format(format_name, **kwargs)
        
        # Ensure directory exists
        dir_path = os.path.dirname(filepath)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
        
        # Write to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(formatted_output)
    
    # === Utility Methods ===
    
    def __len__(self) -> int:
        """Get length of data if applicable."""
        if isinstance(self._data, (list, dict, str)):
            return len(self._data)
        return 1
    
    def __iter__(self) -> Iterator[Any]:
        """Iterate over data if it's iterable."""
        if isinstance(self._data, (list, dict)):
            return iter(self._data)
        else:
            return iter([self._data])
    
    def __getitem__(self, key: Union[int, str, slice]) -> Any:
        """Get item from data."""
        return self._data[key]
    
    def __repr__(self) -> str:
        """String representation of Output object."""
        data_preview = str(self._data)
        if len(data_preview) > 100:
            data_preview = data_preview[:97] + "..."
        return f"Output(type={self._data_type}, data={data_preview})"
    
    def info(self) -> Dict[str, Any]:
        """Get information about this Output object."""
        info = {
            'data_type': self._data_type,
            'metadata': self._metadata,
        }
        
        if isinstance(self._data, list):
            info['length'] = len(self._data)
            if self._data and isinstance(self._data[0], dict):
                info['columns'] = list(self._data[0].keys())
        elif isinstance(self._data, dict):
            info['keys'] = list(self._data.keys())
        
        return info


# === Factory Functions ===

def from_dict(data: Dict[str, Any], **metadata) -> Output:
    """Create Output from dictionary."""
    return Output(data, metadata, 'object')

def from_list(data: List[Any], **metadata) -> Output:
    """Create Output from list."""
    return Output(data, metadata, 'list')

def from_table(data: List[Dict[str, Any]], **metadata) -> Output:
    """Create Output from list of dictionaries (table data)."""
    return Output(data, metadata, 'table')

def from_json(json_str: str, **metadata) -> Output:
    """Create Output from JSON string."""
    try:
        data = json.loads(json_str)
        return Output(data, metadata, 'auto')
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {e}")

def from_csv(csv_str: str, has_headers: bool = True, **kwargs) -> Output:
    """Create Output from CSV string."""
    # Separate metadata from CSV reader kwargs
    metadata = {k: v for k, v in kwargs.items() if k not in ['delimiter', 'quotechar', 'quoting', 'lineterminator', 'escapechar', 'doublequote', 'skipinitialspace']}
    csv_kwargs = {k: v for k, v in kwargs.items() if k in ['delimiter', 'quotechar', 'quoting', 'lineterminator', 'escapechar', 'doublequote', 'skipinitialspace']}
    
    lines = csv_str.strip().split('\n')
    if not lines:
        return Output([], metadata, 'table')
    
    reader = csv.reader(lines, **csv_kwargs)
    rows = list(reader)
    
    if not rows:
        return Output([], {}, 'table')
    
    if has_headers and len(rows) > 1:
        headers = rows[0]
        data = [dict(zip(headers, row)) for row in rows[1:]]
        final_metadata = {**metadata, 'headers': headers}
        return Output(data, final_metadata, 'table')
    else:
        # No headers, create generic column names
        if rows:
            num_cols = len(rows[0])
            headers = [f'col_{i}' for i in range(num_cols)]
            data = [dict(zip(headers, row)) for row in rows]
            final_metadata = {**metadata, 'headers': headers}
            return Output(data, final_metadata, 'table')
        else:
            return Output([], metadata, 'table')

def from_any(data: Any, **metadata) -> Output:
    """Create Output from any data type."""
    return Output(data, metadata, 'auto')

def empty() -> Output:
    """Create empty Output object."""
    return Output(None, {}, 'scalar')