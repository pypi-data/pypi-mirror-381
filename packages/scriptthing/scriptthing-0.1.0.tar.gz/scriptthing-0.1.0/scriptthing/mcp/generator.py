import re
from pathlib import Path
from typing import List, NamedTuple
from scriptthing.metadata import MCPTool 
from jinja2 import Environment, PackageLoader, select_autoescape


def regex_replace(s, pattern, replacement):
	"""Jinja2 filter for regex replacement"""
	return re.sub(pattern, replacement, s)


class ScriptTool(NamedTuple):
	"""Represents a script with its MCP tool metadata"""
	script_path: str
	script_name: str
	tool: MCPTool


class MultiScriptMCPGenerator:
	"""Generator for creating MCP servers with multiple tools from different scripts"""
	
	def __init__(self):
		self.script_tools: List[ScriptTool] = []
		
		# Set up Jinja2 environment
		self.jinja_env = Environment(
			loader=PackageLoader('scriptthing', 'templates'),
			autoescape=select_autoescape(['html', 'xml'])
		)
		# Add custom filters
		self.jinja_env.filters['regex_replace'] = regex_replace
		self.jinja_env.filters['repr'] = repr
	
	def add_script_tool(self, script_path: Path, tool_metadata: MCPTool) -> None:
		"""Add a script and its tool metadata to the server"""
		script_tool = ScriptTool(
			script_path=str(script_path.absolute()),
			script_name=script_path.name,
			tool=tool_metadata
		)
		self.script_tools.append(script_tool)
	
	def generate_mcp_server(self, output_path: Path | None) -> Path:
		"""Generate a complete MCP server file with all added tools"""
		if not self.script_tools:
			raise ValueError("No script tools have been added to the generator")
		
		# Load and render the template
		template = self.jinja_env.get_template('mcp_server_template.jinja2')
		
		# Prepare template context
		import datetime
		import sys
		context = {
			'script_tools': self.script_tools,
			'generated_timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
			'python_executable': sys.executable
		}
		
		# Render the template
		server_code = template.render(context)
		
		# Default output path into repo modules if not provided
		if output_path is None:
			try:
				from scriptthing.repo import ensure_default_repo
				repo = ensure_default_repo()
				output_path = repo.root / 'modules' / 'scriptthing-mcp'
			except Exception:
				output_path = Path.cwd() / 'scriptthing-mcp'
		
		# Write to output file
		with open(output_path, 'w', encoding='utf-8') as f:
			f.write(server_code)
		return output_path



