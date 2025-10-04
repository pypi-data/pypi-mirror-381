"""
Simple base class for scriptthing output formatters.
"""

from abc import ABC, abstractmethod
from typing import Any


class OutputFormatter(ABC):
    """Simple base class for all output formatters."""
    
    def __init__(self, **kwargs):
        self.config = kwargs
    
    @abstractmethod
    def format_data(self, data: Any) -> str:
        """Format data into string representation."""
        pass
    
    @abstractmethod
    def get_content_type(self) -> str:
        """Get MIME content type."""
        pass
    
    @abstractmethod
    def get_file_extension(self) -> str:
        """Get file extension without dot."""
        pass


# Utility functions
def sanitize_filename(name: str) -> str:
    """Sanitize a string for use as filename."""
    import re
    safe_name = re.sub(r'[<>:"/\\|?*]', '_', name)
    safe_name = re.sub(r'[^\w\-_.]', '_', safe_name)
    safe_name = re.sub(r'_+', '_', safe_name)
    return safe_name.strip('_')


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate string to max length with suffix."""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix
