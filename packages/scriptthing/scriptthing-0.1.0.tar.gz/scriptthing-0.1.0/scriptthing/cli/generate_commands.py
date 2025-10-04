import click
from pathlib import Path
from typing import Optional
from scriptthing.templating.paths import list_scripts, get_script_by_name, set_script_permissions
from scriptthing.templating.resources import get_template
from scriptthing.repo import install_internal_repo_if_needed
from scriptthing.shell import open_editor
from scriptthing import utils


@click.group()
def generate() -> None:
    """Generate various scriptthing components"""
    pass


@generate.command()
def bindings() -> None:
    """Generate Python bindings for all scripts"""
    from scriptthing.templating.wrapping import generate_all_script_bindings
    generate_all_script_bindings()
    
    scripts = list_scripts()
    click.secho(f"Generated python bindings for {len(scripts)} scripts")
    if scripts:
        click.secho("Available scripts can be imported as:")
        for script in scripts[:5]:  # Show first 5 as examples
            binding_name: str = script.name.replace("-", "_").replace(".", "_")
            click.secho(f"  from scriptthing.bindings import {binding_name}", fg="blue")
        if len(scripts) > 5:
            click.secho(f"  ... and {len(scripts) - 5} more", fg="blue")


@generate.command()
@click.argument("name", type=click.Choice([p.name for p in list_scripts()]))
@click.option("--edit/--no-edit", type=bool, default=True)
def mcp_metadata(name: str, edit: bool) -> None:
    """Generate MCP metadata for a script"""
    script: Optional[Path] = get_script_by_name(name)

    if not script:
        click.secho("No script found", fg="red")
        return

    script_lines: list[str] = script.read_text().splitlines()
    shebang: str = script_lines[0]
    content: str = "\n".join(script_lines[1:])
    if content.strip().startswith("# MCP"):
        click.secho("Script already has MCP metadata lines", fg="blue")
        return

    comments: str = get_template("metadata_comments.jinja2").render(
        name=script.name,
        path=str(script.absolute())
    )

    full_content: str = "\n".join([shebang, comments, content])
    script.write_text(full_content)

    if edit:
        open_editor(script)


@generate.command()
def mcp_config() -> None:
    """Generate MCP configuration file for existing servers"""
    from scriptthing.mcp.simple_config import SimpleMCPConfigGenerator
    
    generator = SimpleMCPConfigGenerator()
    
    mcp_server_script: Optional[Path] = get_script_by_name("scriptthing-mcp")
    if not mcp_server_script:
        click.secho("You need to generate the MCP server first (scriptthing generate mcp)")
        return 

    success = generator.generate_mcp_entry(mcp_server_script)
    if not success:
        click.secho("No MCP servers found. Generate one first with:", fg="yellow")
        click.secho("scriptthing generate mcp", fg="blue")

    utils.pretty.printjson(success)


@generate.command()
@click.option("--output", "-o", help="Output file path for the MCP server")
def mcp(output: Optional[str] = None) -> None:
    """Generate MCP (Model Context Protocol) server from all scripts with metadata"""
    from scriptthing.mcp import UniversalMCPMetadataParser, MultiScriptMCPGenerator

    generator = MultiScriptMCPGenerator()
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
        default_out = repo.root / 'modules' / 'scriptthing-mcp'
    except Exception:
        default_out = Path(output) if output else Path.cwd() / 'scriptthing-mcp'
    output_path: Path = Path(output or default_out)
    generator.generate_mcp_server(output_path)
    set_script_permissions(output_path)

    click.secho(f"Generated MCP server with {tools_found} tools: {output_path}", fg="green")


# Function to register the generate command group
def register_generate_commands(cli_group: click.Group) -> None:
    """Register the generate command group with the main CLI"""
    cli_group.add_command(generate)