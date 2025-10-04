"""
XML output formatter for scriptthing.

Provides XML output with configurable formatting and structure options.
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom
from typing import Any, Dict, List, Optional
from .base import OutputFormatter, ConfigurableFormatter


class XMLFormatter(ConfigurableFormatter):
    """
    XML formatter with customizable structure and formatting options.
    """
    
    DEFAULT_CONFIG = {
        'root_element': 'data',
        'row_element': 'row',
        'item_element': 'item',
        'key_element': 'key',
        'value_element': 'value',
        'pretty_print': True,
        'indent': '  ',  # Two spaces
        'encoding': 'UTF-8',
        'xml_declaration': True,
        'escape_cdata': True,
        'use_attributes': False,  # Store data as attributes vs. elements
        'attribute_prefix': 'attr_',
        'list_item_name': 'item',
        'preserve_types': True,  # Add type attributes
        'null_representation': 'null',
    }
    
    def get_content_type(self) -> str:
        return 'application/xml'
    
    def get_file_extension(self) -> str:
        return 'xml'
    
    def format_data(self, data: Any) -> str:
        """
        Format data as XML.
        """
        root = ET.Element(self.config['root_element'])
        self._add_data_to_element(root, data)
        
        if self.config['pretty_print']:
            return self._prettify_xml(root)
        else:
            return ET.tostring(root, encoding='unicode')
    
    def format_table(self, data: List[Dict[str, Any]], headers: Optional[List[str]] = None) -> str:
        """
        Format tabular data as XML with row/column structure.
        """
        root = ET.Element(self.config['root_element'])
        
        # Add metadata if headers are provided
        if headers and self.config['preserve_types']:
            headers_elem = ET.SubElement(root, 'headers')
            for header in headers:
                header_elem = ET.SubElement(headers_elem, 'header')
                header_elem.text = header
        
        # Add data rows
        for row_data in data:
            row_elem = ET.SubElement(root, self.config['row_element'])
            
            if self.config['use_attributes']:
                # Store data as attributes
                for key, value in row_data.items():
                    attr_name = f"{self.config['attribute_prefix']}{key}"
                    row_elem.set(attr_name, str(value))
            else:
                # Store data as child elements
                for key, value in row_data.items():
                    self._add_value_to_element(row_elem, key, value)
        
        if self.config['pretty_print']:
            return self._prettify_xml(root)
        else:
            return ET.tostring(root, encoding='unicode')
    
    def _add_data_to_element(self, parent: ET.Element, data: Any, name: Optional[str] = None) -> None:
        """
        Recursively add data to an XML element.
        """
        if isinstance(data, dict):
            # Handle special table structure
            if 'headers' in data and 'rows' in data:
                self._add_table_to_element(parent, data['rows'], data['headers'])
                return
            
            # Handle title/data or title/items structures
            if 'title' in data and 'data' in data:
                if data['title']:
                    title_elem = ET.SubElement(parent, 'title')
                    title_elem.text = str(data['title'])
                self._add_data_to_element(parent, data['data'])
                return
            
            if 'title' in data and 'items' in data:
                if data['title']:
                    title_elem = ET.SubElement(parent, 'title')
                    title_elem.text = str(data['title'])
                self._add_data_to_element(parent, data['items'])
                return
            
            # Regular dictionary
            for key, value in data.items():
                self._add_value_to_element(parent, key, value)
        
        elif isinstance(data, list):
            for item in data:
                item_elem = ET.SubElement(parent, self.config['item_element'])
                self._add_data_to_element(item_elem, item)
        
        else:
            # Scalar value
            if parent.text is None:
                parent.text = self._format_scalar_value(data)
            else:
                # Already has text, create a new element
                value_elem = ET.SubElement(parent, name or 'value')
                value_elem.text = self._format_scalar_value(data)
    
    def _add_table_to_element(self, parent: ET.Element, rows: List[Dict[str, Any]], headers: List[str]) -> None:
        """Add table data to element."""
        # Create headers section
        if headers and self.config['preserve_types']:
            headers_elem = ET.SubElement(parent, 'headers')
            for header in headers:
                header_elem = ET.SubElement(headers_elem, 'header')
                header_elem.text = header
        
        # Create rows section
        for row_data in rows:
            row_elem = ET.SubElement(parent, self.config['row_element'])
            for key, value in row_data.items():
                self._add_value_to_element(row_elem, key, value)
    
    def _add_value_to_element(self, parent: ET.Element, key: str, value: Any) -> None:
        """Add a key-value pair to an element."""
        # Sanitize key name for XML
        element_name = self._sanitize_xml_name(key)
        
        if self.config['use_attributes'] and self._is_simple_value(value):
            # Store as attribute
            parent.set(element_name, str(value))
        else:
            # Store as child element
            child_elem = ET.SubElement(parent, element_name)
            
            if self.config['preserve_types']:
                child_elem.set('type', type(value).__name__)
            
            if isinstance(value, (dict, list)):
                self._add_data_to_element(child_elem, value)
            else:
                child_elem.text = self._format_scalar_value(value)
    
    def _format_scalar_value(self, value: Any) -> str:
        """Format a scalar value for XML content."""
        if value is None:
            return self.config['null_representation']
        elif isinstance(value, bool):
            return 'true' if value else 'false'
        elif isinstance(value, (int, float)):
            return str(value)
        else:
            text = str(value)
            if self.config['escape_cdata'] and any(char in text for char in ['<', '>', '&']):
                return f'<![CDATA[{text}]]>'
            return text
    
    def _is_simple_value(self, value: Any) -> bool:
        """Check if value is simple enough to store as an attribute."""
        return isinstance(value, (str, int, float, bool)) and value is not None
    
    def _sanitize_xml_name(self, name: str) -> str:
        """
        Sanitize a string to be a valid XML element/attribute name.
        """
        import re
        # Remove invalid characters and ensure it starts with letter or underscore
        sanitized = re.sub(r'[^a-zA-Z0-9_.-]', '_', str(name))
        if sanitized and sanitized[0].isdigit():
            sanitized = '_' + sanitized
        return sanitized or 'unnamed'
    
    def _prettify_xml(self, element: ET.Element) -> str:
        """
        Format XML with pretty printing.
        """
        rough_string = ET.tostring(element, encoding='unicode')
        reparsed = minidom.parseString(rough_string)
        
        if self.config['xml_declaration']:
            pretty = reparsed.toprettyxml(indent=self.config['indent'], encoding=None)
            # Remove the first line if it's the XML declaration and we want to control it
            lines = pretty.split('\n')
            if lines[0].startswith('<?xml'):
                lines[0] = f'<?xml version="1.0" encoding="{self.config["encoding"]}"?>'
            return '\n'.join(lines)
        else:
            # Get pretty XML without declaration
            pretty = reparsed.documentElement.toprettyxml(indent=self.config['indent'])
            return pretty


class CompactXMLFormatter(XMLFormatter):
    """
    Compact XML formatter with minimal whitespace.
    """
    
    DEFAULT_CONFIG = {
        **XMLFormatter.DEFAULT_CONFIG,
        'pretty_print': False,
        'xml_declaration': False,
    }


class AttributeXMLFormatter(XMLFormatter):
    """
    XML formatter that prefers attributes over elements.
    """
    
    DEFAULT_CONFIG = {
        **XMLFormatter.DEFAULT_CONFIG,
        'use_attributes': True,
        'preserve_types': False,
    }


class CustomStructureXMLFormatter(XMLFormatter):
    """
    XML formatter with customizable element names.
    """
    
    def __init__(self, root_name: str = 'data', item_name: str = 'item', **kwargs):
        kwargs.update({
            'root_element': root_name,
            'item_element': item_name,
            'row_element': item_name,
        })
        super().__init__(**kwargs)


class SOAPLikeXMLFormatter(XMLFormatter):
    """
    XML formatter that creates SOAP-like envelope structure.
    """
    
    DEFAULT_CONFIG = {
        **XMLFormatter.DEFAULT_CONFIG,
        'root_element': 'envelope',
        'use_namespaces': True,
        'namespace_prefix': 'st',
        'namespace_uri': 'http://scriptthing.example.com/output',
    }
    
    def format_data(self, data: Any) -> str:
        """Format data with SOAP-like envelope."""
        # Create envelope with namespace
        if self.config.get('use_namespaces'):
            root = ET.Element(f"{{{self.config['namespace_uri']}}}{self.config['root_element']}")
            root.set(f'xmlns:{self.config["namespace_prefix"]}', self.config['namespace_uri'])
        else:
            root = ET.Element(self.config['root_element'])
        
        # Add header
        header = ET.SubElement(root, 'header')
        header_timestamp = ET.SubElement(header, 'timestamp')
        from datetime import datetime
        header_timestamp.text = datetime.now().isoformat()
        
        # Add body
        body = ET.SubElement(root, 'body')
        self._add_data_to_element(body, data)
        
        if self.config['pretty_print']:
            return self._prettify_xml(root)
        else:
            return ET.tostring(root, encoding='unicode')