"""
MCP (Model Context Protocol) commands for scriptthing CLI
"""

import subprocess
import sys
from pathlib import Path
from typing import Optional
import click
from scriptthing.repo import ensure_default_repo
from scriptthing.templating.paths import list_scripts, set_script_permissions
from scriptthing.mcp import UniversalMCPMetadataParser, ShellMCPConfigGenerator
from scriptthing.repo import install_internal_repo_if_needed


@click.group()
def mcp() -> None:
    """MCP (Model Context Protocol) server management"""
    pass


@mcp.command()
@click.option("--config", "-c", help="Path to YAML configuration file")
@click.option("--port", "-p", type=int, help="Port to run the server on")
@click.option("--host", help="Host to bind the server to")
def run(config: Optional[str] = None, port: Optional[int] = None, host: Optional[str] = None) -> None:
    """Run the MCP server using shellmcp"""
    
    # Determine config file path
    if config:
        config_path = Path(config)
    else:
        # Try to find the default generated config
        try:
            repo = ensure_default_repo()
            config_path = repo.root / 'config' / 'scriptthing-mcp.yml'
        except Exception:
            config_path = Path.cwd() / 'scriptthing-mcp.yml'
    
    # Check if config file exists
    if not config_path.exists():
        click.secho(f"Configuration file not found: {config_path}", fg="red")
        click.secho("Generate the MCP configuration first with:", fg="yellow")
        click.secho("scriptthing mcp generate", fg="blue")
        return
    
    # Build shellmcp command
    cmd = ["shellmcp", "run", "--config_file", str(config_path)]
    
    # Add optional arguments
    if port:
        cmd.extend(["--port", str(port)])
    if host:
        cmd.extend(["--host", host])
    
    click.secho(f"Starting MCP server with config: {config_path}", fg="green")
    click.secho(f"Command: {' '.join(cmd)}", fg="blue")
    
    try:
        # Run shellmcp
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        click.secho(f"Failed to start MCP server: {e}", fg="red")
        sys.exit(1)
    except KeyboardInterrupt:
        click.secho("\nMCP server stopped", fg="yellow")
    except FileNotFoundError:
        click.secho("shellmcp not found. Install it with:", fg="red")
        click.secho("pip install shellmcp", fg="blue")
        sys.exit(1)


@mcp.command()
@click.option("--config", "-c", help="Path to YAML configuration file")
def validate(config: Optional[str] = None) -> None:
    """Validate the MCP configuration file"""
    
    # Determine config file path
    if config:
        config_path = Path(config)
    else:
        # Try to find the default generated config
        try:
            repo = ensure_default_repo()
            config_path = repo.root / 'config' / 'scriptthing-mcp.yml'
        except Exception:
            config_path = Path.cwd() / 'scriptthing-mcp.yml'
    
    # Check if config file exists
    if not config_path.exists():
        click.secho(f"Configuration file not found: {config_path}", fg="red")
        return
    
    # Build shellmcp validate command
    cmd = ["shellmcp", "validate", str(config_path)]
    
    click.secho(f"Validating MCP configuration: {config_path}", fg="green")
    
    try:
        # Run shellmcp validate
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        click.secho("✓ Configuration is valid", fg="green")
        if result.stdout:
            click.echo(result.stdout)
    except subprocess.CalledProcessError as e:
        click.secho("✗ Configuration validation failed", fg="red")
        if e.stdout:
            click.echo(e.stdout)
        if e.stderr:
            click.echo(e.stderr)
        sys.exit(1)
    except FileNotFoundError:
        click.secho("shellmcp not found. Install it with:", fg="red")
        click.secho("pip install shellmcp", fg="blue")
        sys.exit(1)


@mcp.command()
@click.option("--output", "-o", help="Output file path for the MCP server")
def generate(output: Optional[str] = None) -> None:
    """Generate MCP (Model Context Protocol) server from all scripts with metadata"""
    generator = ShellMCPConfigGenerator()
    tools_found: int = 0
    
    for script_path in list_scripts():
        # Use universal parser for all scripts (supports all languages)
        parser = UniversalMCPMetadataParser(script_path)
        tool_metadata = parser.parse()
        
        if tool_metadata:
            generator.add_script_tool(script_path, tool_metadata)
            tools_found += 1
    
    if tools_found == 0:
        click.secho("No scripts with MCP metadata found", fg="red")
        click.secho("Add metadata to your scripts using the universal format:", fg="yellow")
        click.secho("  # MCP_NAME: tool_name", fg="blue")
        click.secho("  # MCP_DESCRIPTION: Tool description", fg="blue")
        click.secho("  # MCP_PARAM: name:type:description:required", fg="blue")
        click.secho("", fg="blue")
        click.secho("Use '//' instead of '#' for JavaScript, Go, Rust, etc.", fg="cyan")
        return

    internal_repo = install_internal_repo_if_needed()
    if internal_repo and internal_repo.scripts_dir.exists():
        for script_path in internal_repo.scripts_dir.glob("*"):
            if not script_path.is_file():
                continue
            parser = UniversalMCPMetadataParser(script_path)
            tool_metadata = parser.parse()
            if tool_metadata:
                generator.add_script_tool(script_path, tool_metadata)

    
    try:
        from scriptthing.repo import ensure_default_repo
        repo = ensure_default_repo()
        default_out = repo.root / 'config' / 'scriptthing-mcp.yml'
    except Exception:
        default_out = Path(output) if output else Path.cwd() / 'scriptthing-mcp.yml'
    output_path: Path = Path(output or default_out)
    generator.generate_config(output_path)
    set_script_permissions(output_path)

    click.secho(f"Generated MCP server with {tools_found} tools: {output_path}", fg="green")


def register_mcp_commands(cli_group: click.Group) -> None:
    """Register MCP commands with the main CLI"""
    cli_group.add_command(mcp)
