"""
scriptthing.output - Output formatting utilities for scriptthing

This package provides utilities for creating script outputs in various formats
including text, JSON, CSV, XML, HTML, Markdown, and YAML.

Basic usage:
    from scriptthing.output import from_dict, from_table
    
    # Create Output objects from any data source
    data = from_dict({'name': 'John', 'age': 30})
    table = from_table([
        {'name': 'Alice', 'age': 25, 'city': 'New York'},
        {'name': 'Bob', 'age': 30, 'city': 'San Francisco'}
    ])
    
    # Transform data with method chaining
    result = table.filter(lambda x: x['age'] > 25).sort('name')
    
    # Render in any format
    json_output = data.as_json()
    html_output = result.as_html()

Advanced usage:
    from scriptthing.output import from_csv, get_formatter
    
    # Load from various sources
    csv_data = from_csv("name,age\nJohn,30\nJane,25")
    
    # Process and transform
    adults = csv_data.filter(lambda x: int(x['age']) >= 18)
    
    # Output with custom formatting
    html_output = adults.as_html(dark_mode=True, sortable_table=True)
"""

# Import base classes
from .base import (
    OutputFormatter,
    TableFormatter,
    ConfigurableFormatter,
    sanitize_filename,
    truncate_string
)

# Import specific formatters
from .text import TextFormatter
from .json_formatter import JSONFormatter, JSONLinesFormatter
from .csv import (
    CSVFormatter,
    TSVFormatter, 
    ExcelCSVFormatter,
    PipeDelimitedFormatter,
    CustomDelimiterCSVFormatter
)
from .xml import (
    XMLFormatter,
    CompactXMLFormatter,
    AttributeXMLFormatter,
    CustomStructureXMLFormatter
)
from .html import (
    HTMLFormatter,
    MinimalHTMLFormatter,
    BootstrapHTMLFormatter
)
from .markdown import (
    MarkdownFormatter,
    GitHubMarkdownFormatter,
    SimpleMarkdownFormatter,
    WikiMarkdownFormatter
)
from .yaml_formatter import DefaultYAMLFormatter

# Try to import YAML formatters (may not be available)
try:
    from .yaml_formatter import (
        YAMLFormatter,
        CompactYAMLFormatter,
        VerboseYAMLFormatter,
        LiteralYAMLFormatter,
        FoldedYAMLFormatter
    )
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

# Import manager and convenience functions
from .manager import (
    OutputManager,
    output_manager,
    get_available_formats,
    get_formatter
)

# Import new Output class and factory functions
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

# Version info
__version__ = '0.1.0'
__author__ = 'scriptthing'

# Define public API
__all__ = [
        # Base classes
    'OutputFormatter',
    'TableFormatter',
    'ConfigurableFormatter',
    
    # Text formatters
    'TextFormatter',
    
    # JSON formatters
    'JSONFormatter',
    'JSONLinesFormatter',
    
    # CSV formatters
    'CSVFormatter',
    'TSVFormatter',
    'ExcelCSVFormatter',
    'PipeDelimitedFormatter',
    'CustomDelimiterCSVFormatter',
    
    # XML formatters
    'XMLFormatter',
    'CompactXMLFormatter',
    'AttributeXMLFormatter',
    'CustomStructureXMLFormatter',
    
    # HTML formatters
    'HTMLFormatter',
    'MinimalHTMLFormatter',
    'BootstrapHTMLFormatter',
    
    # Markdown formatters
    'MarkdownFormatter',
    'GitHubMarkdownFormatter',
    'SimpleMarkdownFormatter',
    'WikiMarkdownFormatter',
    
    # YAML formatters (base)
    'DefaultYAMLFormatter',
    
    # Manager and convenience functions
    'OutputManager',
    'output_manager',
    'get_available_formats',
    'get_formatter',
    
    # Output class and factory functions
    'Output',
    'from_dict',
    'from_list',
    'from_table',
    'from_json',
    'from_csv',
    'from_any',
    'empty',
    
    # Utility functions
    'sanitize_filename',
    'truncate_string',
    
    # Constants
    'HAS_YAML',
]

# Add YAML formatters to __all__ if available
if HAS_YAML:
    __all__.extend([
        'YAMLFormatter',
        'CompactYAMLFormatter',
        'VerboseYAMLFormatter',
        'LiteralYAMLFormatter',
        'FoldedYAMLFormatter',
    ])


def get_version() -> str:
    """Get the version of the output package."""
    return __version__


def list_formatters(detailed: bool = False) -> dict:
    """
    List all available formatters.
    
    Args:
        detailed: If True, return detailed information about each formatter
        
    Returns:
        dict: Formatter information
    """
    if detailed:
        return output_manager.get_formatter_info()
    else:
        return {
            'available_formats': get_available_formats(),
            'has_yaml': HAS_YAML,
            'default_format': output_manager.get_default_format()
        }


def quick_format(data, format_name: str = 'text') -> str:
    """
    Quick format function with sensible defaults.
    
    Args:
        data: Data to format
        format_name: Format to use
        
    Returns:
        str: Formatted output
    """
    return from_any(data).as_format(format_name)


# Examples for documentation
def _example_usage():
    """Examples of how to use the output package."""
    
    # Sample data
    sample_data = [
        {'name': 'Alice', 'age': 25, 'city': 'New York', 'score': 95.5},
        {'name': 'Bob', 'age': 30, 'city': 'San Francisco', 'score': 87.2},
        {'name': 'Charlie', 'age': 35, 'city': 'Chicago', 'score': 92.1}
    ]
    
    examples = {}
    
    # Create Output object
    output = from_table(sample_data)
    
    # Text table
    examples['text'] = output.as_text()
    
    # JSON output
    examples['json'] = output.as_json(indent=2)
    
    # CSV output
    examples['csv'] = output.as_csv()
    
    # HTML table
    examples['html'] = output.as_html(page_title='Sample Data', striped_rows=True)
    
    # Markdown table
    examples['markdown'] = output.as_markdown()
    
    return examples


if __name__ == '__main__':
    # Print package info when run as module
    print(f"scriptthing.output v{__version__}")
    print(f"Available formats: {', '.join(get_available_formats())}")
    print(f"YAML support: {'Yes' if HAS_YAML else 'No'}")
    
    # Show example usage
    print("\nExample outputs:")
    examples = _example_usage()
    for format_name, output in examples.items():
        print(f"\n--- {format_name.upper()} ---")
        print(output[:200] + "..." if len(output) > 200 else output)