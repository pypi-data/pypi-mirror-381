"""
Common format detection and parsing for scriptthing.

Provides unified format detection and data type properties that can be used
across stdin, output, parallel, and other modules.
"""

import json
from abc import ABC, abstractmethod
from functools import cached_property
from pathlib import Path
from typing import List, Dict, Any, Union, Optional, Iterator


class DataParser(ABC):
    """Base class for data parsing with cached properties for different formats."""
    
    def __init__(self, raw_data: Union[str, bytes]):
        """Initialize with raw data."""
        if isinstance(raw_data, bytes):
            self._raw_text = raw_data.decode('utf-8')
        else:
            self._raw_text = raw_data
    
    @cached_property
    def text(self) -> str:
        """Get data as plain text."""
        return self._raw_text
    
    @cached_property
    def lines(self) -> List[str]:
        """Get data as list of lines."""
        return [line.rstrip('\n\r') for line in self._raw_text.splitlines()]
    
    @cached_property
    def json(self) -> Union[Dict[str, Any], List[Any]]:
        """Parse data as JSON."""
        return json.loads(self._raw_text)
    
    @cached_property
    def jsonl(self) -> List[Dict[str, Any]]:
        """Parse data as JSON Lines (JSONL)."""
        return [json.loads(line) for line in self.lines if line.strip()]
    
    @cached_property
    def csv_rows(self) -> List[Dict[str, str]]:
        """Parse data as CSV with headers."""
        if not self.lines:
            return []
        headers = [h.strip() for h in self.lines[0].split(',')]
        rows = []
        for line in self.lines[1:]:
            if line.strip():
                values = [v.strip() for v in line.split(',')]
                rows.append(dict(zip(headers, values)))
        return rows
    
    @cached_property
    def words(self) -> List[List[str]]:
        """Get data as list of word lists (one per line)."""
        return [line.split() for line in self.lines if line.strip()]
    
    def words_with_separator(self, separator: str) -> List[List[str]]:
        """Get data as word lists using custom separator."""
        return [line.split(separator) for line in self.lines if line.strip()]
    
    @cached_property
    def detected_format(self) -> str:
        """Auto-detect the most likely data format."""
        text = self._raw_text.strip()
        if not text:
            return "empty"
        
        # Try JSON first
        try:
            parsed = json.loads(text)
            if isinstance(parsed, list):
                return "json_array"
            elif isinstance(parsed, dict):
                return "json_object"
            else:
                return "json_value"
        except json.JSONDecodeError:
            pass
        
        lines = self.lines
        if not lines:
            return "empty"
        
        # Check if JSONL
        if len(lines) >= 1 and all(self._is_json_line(line) for line in lines[:3] if line.strip()):
            return "jsonl"
        
        # Check if CSV
        if len(lines) > 1 and ',' in lines[0]:
            first_cols = len(lines[0].split(','))
            if all(len(line.split(',')) == first_cols for line in lines[:3] if line.strip()):
                return "csv"
        
        # Default to text
        return "text"
    
    def _is_json_line(self, line: str) -> bool:
        """Check if a line is valid JSON."""
        try:
            json.loads(line.strip())
            return True
        except json.JSONDecodeError:
            return False
    



def create_items_for_parallel(
    data: str, 
    chunk_size: Optional[int] = None, 
    separator: Optional[str] = None
) -> Iterator[tuple[str, Dict[str, Any]]]:
    """
    Create items for parallel processing using unified format detection.
    
    Args:
        data: Input data as string
        chunk_size: If specified, process in chunks instead of individual items
        separator: Custom separator for text lines
        
    Yields:
        (data_item, fields) tuples for parallel processing
    """
    parser = DataParser(data)
    format_type = parser.detected_format
    
    if format_type == "json_array":
        json_data = parser.json
        if chunk_size:
            # Chunked JSON processing
            for i in range(0, len(json_data), chunk_size):
                chunk = json_data[i:i + chunk_size]
                yield (json.dumps(chunk), {})
        else:
            # Individual JSON objects
            for obj in json_data:
                fields = obj if isinstance(obj, dict) else {"_1": obj}
                if isinstance(obj, dict):
                    for i, (k, v) in enumerate(obj.items(), 1):
                        fields[f'_{i}'] = v
                yield (json.dumps(obj), fields)
    
    elif format_type == "jsonl":
        if chunk_size:
            # Chunked JSONL processing
            lines = parser.lines
            for i in range(0, len(lines), chunk_size):
                chunk_lines = lines[i:i + chunk_size]
                yield ('\n'.join(chunk_lines), {})
        else:
            # Individual JSONL records
            for line in parser.lines:
                if line.strip():
                    try:
                        obj = json.loads(line)
                        fields = obj if isinstance(obj, dict) else {"_1": line}
                        if isinstance(obj, dict):
                            for i, (k, v) in enumerate(obj.items(), 1):
                                fields[f'_{i}'] = v
                        yield (line, fields)
                    except json.JSONDecodeError:
                        yield (line, {"_1": line})
    
    elif format_type == "csv":
        csv_data = parser.csv_rows
        if chunk_size:
            # Chunked CSV processing
            headers = list(csv_data[0].keys()) if csv_data else []
            header_line = ','.join(headers)
            data_lines = [','.join(row.values()) for row in csv_data]
            
            for i in range(0, len(data_lines), chunk_size):
                chunk_lines = data_lines[i:i + chunk_size]
                chunk_data = header_line + '\n' + '\n'.join(chunk_lines)
                yield (chunk_data, {})
        else:
            # Individual CSV rows
            for row in csv_data:
                fields = row.copy()
                # Add positional fields
                for i, value in enumerate(row.values(), 1):
                    fields[f'_{i}'] = value
                row_line = ','.join(row.values())
                yield (row_line, fields)
    
    else:
        # Text lines (default)
        lines = parser.lines
        if chunk_size:
            # Chunked text processing
            for i in range(0, len(lines), chunk_size):
                chunk_lines = lines[i:i + chunk_size]
                yield ('\n'.join(chunk_lines), {})
        else:
            # Individual text lines with word-based positional variables
            for i, line in enumerate(lines):
                if line.strip():
                    words = line.split(separator) if separator else line.split()
                    fields = {
                        "line": line,
                        "index": i,
                        "length": len(line),
                        "words": len(words),
                        "upper": line.upper(),
                        "lower": line.lower()
                    }
                    # Add positional fields for words
                    for pos, word in enumerate(words, 1):
                        fields[f'_{pos}'] = word.strip()
                    yield (line, fields)


# Convenience functions for backward compatibility
def detect_format(data: str) -> str:
    """Detect format of input data."""
    return DataParser(data).detected_format


def parse_as_json(data: str) -> Union[Dict[str, Any], List[Any]]:
    """Parse data as JSON."""
    return DataParser(data).json


def parse_as_jsonl(data: str) -> List[Dict[str, Any]]:
    """Parse data as JSONL."""
    return DataParser(data).jsonl


def parse_as_csv(data: str) -> List[Dict[str, str]]:
    """Parse data as CSV."""
    return DataParser(data).csv_rows


def parse_as_lines(data: str) -> List[str]:
    """Parse data as lines."""
    return DataParser(data).lines