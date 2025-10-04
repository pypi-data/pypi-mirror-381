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
    
    # === Output Rendering Methods ===
    
    def as_format(self, format_name: str, **kwargs) -> str:
        """Render using any available format."""
        formatter = output_manager.get_formatter(format_name, **kwargs)
        return formatter.format_data(self._data)
    
    def as_json(self, **kwargs) -> str:
        """Render as JSON format."""
        return self.as_format('json', **kwargs)
    
    def as_csv(self, **kwargs) -> str:
        """Render as CSV format."""
        return self.as_format('csv', **kwargs)
    
    def as_text(self, **kwargs) -> str:
        """Render as formatted text."""
        return self.as_format('text', **kwargs)
    
    def __repr__(self) -> str:
        """String representation."""
        data_preview = str(self._data)[:100]
        return f"Output({self._data_type}: {data_preview}...)"


# Factory functions
def from_dict(data: Dict[str, Any]) -> Output:
    """Create Output from dictionary."""
    return Output(data, {}, 'object')

def from_list(data: List[Any]) -> Output:
    """Create Output from list."""
    return Output(data, {}, 'list')

def from_table(data: List[Dict[str, Any]]) -> Output:
    """Create Output from table data."""
    return Output(data, {}, 'table')

def from_json(json_str: str) -> Output:
    """Create Output from JSON string."""
    return Output(json.loads(json_str), {}, 'auto')

def from_csv(csv_str: str, has_headers: bool = True) -> Output:
    """Create Output from CSV string."""
    reader = csv.reader(csv_str.strip().split('\n'))
    rows = list(reader)
    if has_headers and len(rows) > 1:
        headers = rows[0]
        data = [dict(zip(headers, row)) for row in rows[1:]]
        return Output(data, {}, 'table')
    return Output([{'col_' + str(i): v for i, v in enumerate(row)} for row in rows], {}, 'table')

def from_any(data: Any) -> Output:
    """Create Output from any data."""
    return Output(data, {}, 'auto')

def empty() -> Output:
    """Create empty Output."""
    return Output([], {}, 'list')
