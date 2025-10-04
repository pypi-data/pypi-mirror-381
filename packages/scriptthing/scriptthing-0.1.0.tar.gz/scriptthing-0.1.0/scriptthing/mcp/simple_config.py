#!/usr/bin/env python3

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional

class SimpleMCPConfigGenerator:
	"""Simple MCP configuration file generator"""
	
	def __init__(self):
		self.python_executable = sys.executable
	
	def find_mcp_servers(self) -> List[Path]:
		"""Find MCP server files in current directory"""
		current_dir = Path.cwd()
		return list(current_dir.glob("mcp_server*.py"))

	def generate_mcp_entry(self, server_path: Path) -> Dict:
		return {
			"command": self.python_executable,
			"args": [str(server_path.absolute())],
			"description": f"Scriptthing tools from {server_path.name}",
			"disabled": False
		}

	
	def generate_amazon_q_config(self, server_paths: List[Path]) -> Dict:
		"""Generate Amazon Q mcp.json configuration"""
		config = {"mcpServers": {}}
		
		for server_path in server_paths:
			server_name = server_path.stem.replace('_', '-')
			config["mcpServers"][server_name] = {
				"command": self.python_executable,
				"args": [str(server_path.absolute())],
				"description": f"Scriptthing tools from {server_path.name}",
				"disabled": False
			}
		
		return config
	
	def save_config(self, config: Dict, output_path: Path) -> bool:
		"""Save configuration to file"""
		try:
			output_path.parent.mkdir(parents=True, exist_ok=True)
			with open(output_path, 'w', encoding='utf-8') as f:
				json.dump(config, f, indent=2)
			return True
		except Exception as e:
			print(f"Error saving config: {e}")
			return False
	
	def generate_config_file(self, output_path: Optional[Path] = None) -> bool:
		"""Generate Amazon Q configuration file"""
		if output_path is None:
			# Default to repo modules config dir
			try:
				from scriptthing.repo import ensure_default_repo
				repo = ensure_default_repo()
				output_path = repo.root / 'modules' / 'mcp.json'
			except Exception:
				output_path = Path.cwd() / "mcp.json"
		
		server_paths = self.find_mcp_servers()
		if not server_paths:
			print("No MCP servers found in current directory")
			return False
		
		config = self.generate_amazon_q_config(server_paths)
		
		if self.save_config(config, output_path):
			print(f"✓ Generated MCP configuration: {output_path}")
			print(f"Found {len(server_paths)} MCP server(s):")
			for path in server_paths:
				print(f"  - {path.name}")
			return True
		
		return False


def main():
	"""CLI entry point"""
	import argparse
	
	parser = argparse.ArgumentParser(description="Generate MCP configuration file")
	parser.add_argument('--output', '-o', type=Path, help='Output file path (default: repo modules mcp.json)')
	
	args = parser.parse_args()
	
	generator = SimpleMCPConfigGenerator()
	success = generator.generate_config_file(args.output)
	
	if success:
		print("\nTo use with Amazon Q:")
		print("1. Copy mcp.json to your project directory")
		print("2. Configure Amazon Q to use the MCP servers")
	else:
		print("Failed to generate configuration file")


if __name__ == "__main__":
	main()
