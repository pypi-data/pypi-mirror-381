import sys
import yaml
from pathlib import Path
from typing import List, NamedTuple, Dict, Any
from scriptthing.metadata import MCPTool, Parameter


class ScriptTool(NamedTuple):
	"""Represents a script with its MCP tool metadata"""
	script_path: str
	script_name: str
	tool: MCPTool


class ShellMCPConfigGenerator:
	"""Generator for creating shellmcp-compatible YAML configuration files"""
	
	def __init__(self):
		self.script_tools: List[ScriptTool] = []
	
	def add_script_tool(self, script_path: Path, tool_metadata: MCPTool) -> None:
		"""Add a script and its tool metadata to the server"""
		script_tool = ScriptTool(
			script_path=str(script_path.absolute()),
			script_name=script_path.name,
			tool=tool_metadata
		)
		self.script_tools.append(script_tool)
	
	def generate_config(self, output_path: Path | None) -> Path:
		"""Generate a shellmcp-compatible YAML configuration file"""
		if not self.script_tools:
			raise ValueError("No script tools have been added to the generator")
		
		# Default output path into repo config directory if not provided
		if output_path is None:
			try:
				from scriptthing.repo import ensure_default_repo
				repo = ensure_default_repo()
				# Create config directory if it doesn't exist
				config_dir = repo.root / 'config'
				config_dir.mkdir(exist_ok=True)
				output_path = config_dir / 'scriptthing-mcp.yml'
			except Exception:
				output_path = Path.cwd() / 'scriptthing-mcp.yml'
		
		# Ensure output path has .yml or .yaml extension
		if not output_path.suffix.lower() in ['.yml', '.yaml']:
			output_path = output_path.with_suffix('.yml')
		
		# Build the YAML configuration
		config = self._build_yaml_config()
		
		# Ensure output directory exists
		output_path.parent.mkdir(parents=True, exist_ok=True)
		
		# Write YAML to output file
		with open(output_path, 'w', encoding='utf-8') as f:
			yaml.dump(config, f, default_flow_style=False, sort_keys=False, width=float('inf'))
		
		return output_path
	
	def _build_yaml_config(self) -> Dict[str, Any]:
		"""Build the YAML configuration structure"""
		config = {
			'server': {
				'name': 'scriptthing-server',
				'desc': 'ScriptThing MCP Server',
				'version': '1.0.0'
			},
			'tools': {}
		}
		
		# Add each script tool to the configuration
		for script_tool in self.script_tools:
			tool_name = script_tool.tool.name
			tool_config = {
				'desc': script_tool.tool.description,
				'cmd': self._build_command_string(script_tool),
				'args': self._build_args_list(script_tool.tool.parameters),
				'help-cmd': f"{sys.executable} {script_tool.script_path} --help"
			}
			
			# Add AI instructions if present
			if script_tool.tool.ai_instructions_before:
				tool_config['ai_instructions_before'] = script_tool.tool.ai_instructions_before
			if script_tool.tool.ai_instructions_after:
				tool_config['ai_instructions_after'] = script_tool.tool.ai_instructions_after
			
			config['tools'][tool_name] = tool_config
		
		return config
	
	def _build_command_string(self, script_tool: ScriptTool) -> str:
		"""Build the command string for executing the script"""
		# Determine execution method based on script type
		script_path = Path(script_tool.script_path)
		
		# Check if it's a bash script (has shebang or .sh extension)
		if script_path.suffix == '.sh' or self._is_bash_script(script_path):
			# Execute bash script directly
			cmd_parts = [str(script_path)]
		else:
			# Use Python executable for other scripts
			cmd_parts = [sys.executable, str(script_path)]
		
		# Add command-line arguments for each parameter
		for param in script_tool.tool.parameters:
			if param.type == 'boolean':
				# For boolean parameters, use conditional flag format
				# Only include the flag if the value is true
				cmd_parts.append(f"{{% if {param.name} %}}--{param.name}{{% endif %}}")
			else:
				# For other types, use key-value format
				cmd_parts.append(f"--{param.name} '{{{{{param.name}}}}}'")
		
		return ' '.join(cmd_parts)
	
	def _build_args_list(self, parameters: List[Parameter]) -> List[Dict[str, Any]]:
		"""Build the args list for shellmcp"""
		args = []
		for param in parameters:
			arg_dict = {
				'name': param.name,
				'help': param.description,
				'type': param.type
			}
			
			# Add required field if not required
			if not param.required:
				arg_dict['required'] = False
			
			# Add default value if present
			if param.default is not None:
				arg_dict['default'] = param.default
			
			# Add enum values if present
			if param.enum:
				arg_dict['enum'] = param.enum
			
			args.append(arg_dict)
		
		return args
	
	def _is_bash_script(self, script_path: Path) -> bool:
		"""Check if a script is a bash script by examining the shebang"""
		try:
			with open(script_path, 'r', encoding='utf-8') as f:
				first_line = f.readline().strip()
				return first_line.startswith('#!/usr/bin/env bash') or first_line.startswith('#!/bin/bash')
		except Exception:
			return False



