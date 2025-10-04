#!/usr/bin/env python3
"""
Universal MCP Metadata Parser

Parses YAML-like MCP metadata from comments in any programming language.
Supports different comment styles: #, //, /* */, etc.
"""

import re
from pathlib import Path
from typing import Optional, List, Dict, Any
from scriptthing.metadata import MCPTool, Parameter


class UniversalMCPMetadataParser:
    """Universal parser for YAML-like MCP metadata in any language"""
    
    # Comment patterns for different languages
    COMMENT_PATTERNS = {
        '.py': r'^\s*#\s*',     # Python: # comment
        '.sh': r'^\s*#\s*',     # Shell: # comment
        '.ts': r'^\s*//\s*',    # TypeScript: // comment
        '.java': r'^\s*//\s*',  # Java: // comment
        '.cpp': r'^\s*//\s*',   # C++: // comment
        '.c': r'^\s*//\s*',     # C: // comment
        '.cs': r'^\s*//\s*',    # C#: // comment
        '.php': r'^\s*//\s*',   # PHP: // comment
        '.rb': r'^\s*#\s*',     # Ruby: # comment
        '.pl': r'^\s*#\s*',     # Perl: # comment
        '.go': r'^\s*//\s*',    # Go: // comment
        '.rs': r'^\s*//\s*',    # Rust: // comment
    }
    
    def __init__(self, script_path: Path):
        self.script_path = script_path
        self.file_extension = script_path.suffix.lower()
        
        # Determine comment pattern based on file extension
        self.comment_pattern = self.COMMENT_PATTERNS.get(
            self.file_extension, 
            r'^\s*#\s*'  # Default to # comments
        )
        
    def parse(self) -> Optional[MCPTool]:
        """Parse the script and extract MCP tool metadata"""
        try:
            with open(self.script_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            return self._find_mcp_metadata(content)
            
        except Exception:
            return None
    
    def _find_mcp_metadata(self, content: str) -> Optional[MCPTool]:
        """Find MCP metadata using YAML-like format in comments"""
        yaml_metadata = self._parse_yaml_like_comments(content)
        if yaml_metadata:
            return self._parse_metadata_dict(yaml_metadata)
        
        return None
    
    def _parse_yaml_like_comments(self, content: str) -> Optional[Dict[str, Any]]:
        """Parse YAML-like metadata from comments"""
        metadata = {}
        parameters = []
        context_lines = []
        output_lines = []
        
        for line in content.split('\n'):
            # Remove comment prefix and whitespace
            cleaned_line = re.sub(self.comment_pattern, '', line).strip()
            
            if not cleaned_line:
                continue
            
            # Extract MCP_NAME
            name_match = re.match(r'MCP_NAME:\s*(.+)', cleaned_line)
            if name_match:
                metadata['name'] = name_match.group(1).strip()
                continue
            
            # Extract MCP_DESCRIPTION
            desc_match = re.match(r'MCP_DESCRIPTION:\s*(.+)', cleaned_line)
            if desc_match:
                metadata['description'] = desc_match.group(1).strip()
                continue
            
            # Extract MCP_CONTEXT
            context_match = re.match(r'MCP_CONTEXT:\s*(.+)', cleaned_line)
            if context_match:
                metadata['context'] = context_match.group(1).strip()
                continue
            
            # Extract MCP_OUTPUT_INSTRUCTIONS
            output_match = re.match(r'MCP_OUTPUT_INSTRUCTIONS:\s*(.+)', cleaned_line)
            if output_match:
                metadata['output_instructions'] = output_match.group(1).strip()
                continue
            
            # Extract CONTEXT lines (general context comments)
            context_line_match = re.match(r'CONTEXT:\s*(.+)', cleaned_line)
            if context_line_match:
                context_lines.append(context_line_match.group(1).strip())
                continue
            
            # Extract OUTPUT lines (general output comments)
            output_line_match = re.match(r'OUTPUT:\s*(.+)', cleaned_line)
            if output_line_match:
                output_lines.append(output_line_match.group(1).strip())
                continue
            
            # Extract MCP_PARAM: name:type:description:required:enum_values
            param_match = re.match(r'MCP_PARAM:\s*(.+)', cleaned_line)
            if param_match:
                param_str = param_match.group(1).strip()
                param_parts = param_str.split(':')
                if len(param_parts) >= 3:
                    param = {
                        'name': param_parts[0].strip(),
                        'type': param_parts[1].strip() if len(param_parts) > 1 else 'string',
                        'description': param_parts[2].strip(),
                        'required': param_parts[3].strip().lower() == 'true' if len(param_parts) > 3 else True
                    }
                    
                    # Handle enum values
                    if len(param_parts) > 4 and param_parts[4].strip():
                        enum_str = param_parts[4].strip()
                        if enum_str.startswith('[') and enum_str.endswith(']'):
                            # Parse [value1,value2,value3]
                            enum_values = [v.strip() for v in enum_str[1:-1].split(',')]
                            param['enum'] = enum_values
                        else:
                            # Parse comma-separated values
                            param['enum'] = [v.strip() for v in enum_str.split(',')]
                    
                    parameters.append(param)
        
        if 'name' in metadata and 'description' in metadata:
            metadata['parameters'] = parameters
            
            # Combine context from MCP_CONTEXT and CONTEXT lines
            combined_context = []
            if 'context' in metadata:
                combined_context.append(metadata['context'])
            if context_lines:
                combined_context.extend(context_lines)
            if combined_context:
                metadata['context'] = '\n'.join(combined_context)
            
            # Combine output instructions from MCP_OUTPUT_INSTRUCTIONS and OUTPUT lines
            combined_output = []
            if 'output_instructions' in metadata:
                combined_output.append(metadata['output_instructions'])
            if output_lines:
                combined_output.extend(output_lines)
            if combined_output:
                metadata['output_instructions'] = '\n'.join(combined_output)
            
            return metadata
        
        return None
    
    def _parse_metadata_dict(self, metadata: Dict[str, Any]) -> Optional[MCPTool]:
        """Parse metadata dictionary into MCPTool object"""
        try:
            name = metadata.get('name')
            description = metadata.get('description')
            
            if not name or not description:
                return None
            
            # Parse parameters
            parameters = []
            param_data = metadata.get('parameters', [])
            
            for param in param_data:
                if isinstance(param, dict):
                    param_obj = Parameter(
                        name=param.get('name', ''),
                        description=param.get('description', ''),
                        type=param.get('type', 'string'),
                        required=param.get('required', True),
                        enum=param.get('enum'),
                        default=param.get('default')
                    )
                    parameters.append(param_obj)
            
            return MCPTool(
                name=name,
                description=description,
                parameters=parameters,
                ai_instructions_before=metadata.get('context'),
                ai_instructions_after=metadata.get('output_instructions')
            )
            
        except Exception:
            return None


def get_comment_prefix(file_extension: str) -> str:
    """Get the comment prefix for a given file extension"""
    comment_map = {
        '.py': '#',
        '.sh': '#',
        '.ts': '//',
        '.java': '//',
        '.cpp': '//',
        '.c': '//',
        '.cs': '//',
        '.php': '//',
        '.rb': '#',
        '.pl': '#',
        '.go': '//',
        '.rs': '//',
    }
    return comment_map.get(file_extension.lower(), '#')