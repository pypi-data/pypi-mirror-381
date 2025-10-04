from __future__ import annotations

# Added duration parsing, store access, and pretty printing
import click
from datetime import datetime, timedelta
from typing import Any, Dict, Optional
from pathlib import Path

from scriptthing.utils import store
from scriptthing.utils.duration import parse_duration
from scriptthing.utils.pretty import printformatted

from scriptthing.core import ScriptMetadata, OutputType
from scriptthing.templating.paths import _get_internal_script_by_name


@click.group()
def vars() -> None:
    """Manage scriptthing variables"""
    pass


@vars.command()
def show() -> None:
    """Show all variables (and their expiry)."""
    variables: Dict[str, Any] = store._get_all()
    if not variables:
        click.secho("No variables stored", fg="yellow")
        return

    now: datetime = datetime.now()
    for key, meta in variables.items():
        value: Any = meta["value"]
        ttl: Optional[timedelta] = meta["ttl"]
        created_at: datetime = meta["created_at"]

        if ttl is None:
            expires_in: str = "never"
        else:
            expiry_time: datetime = created_at + ttl
            remaining: timedelta = expiry_time - now
            # guard negative
            if remaining.total_seconds() < 0:
                remaining = timedelta(0)
            expires_in = f"{remaining} (at {expiry_time:%Y-%m-%d %H:%M:%S})"

        click.secho(f"{key}: ", fg="blue", nl=False)
        click.secho(value, fg="green", nl=False)
        click.secho(f"  (expires {expires_in})")


@vars.command()
@click.argument("key", type=str)
def get(key: str) -> None:
    """Get a variable value"""
    try:
        value: Any = store.get(key)
        printformatted(value)
    except KeyError:
        click.secho(f"Variable '{key}' not found", fg="red")


@vars.command()
@click.argument("key", type=str)
@click.argument("value", type=str)
@click.option("--ttl", type=str, help="Time to live (e.g., '1h', '30m', '2d')")
def set(key: str, value: str, ttl: Optional[str] = None) -> None:
    """Set a variable with optional TTL"""
    ttl_duration: Optional[timedelta] = None
    if ttl:
        try:
            ttl_duration = parse_duration(ttl)
        except ValueError as e:
            click.secho(f"Invalid TTL format: {e}", fg="red")
            return
    
    store.put(key, value, ttl_duration)
    click.secho(f"Variable '{key}' set", fg="green")
    # Note: IDE bindings are automatically generated in the background


@vars.command()
@click.argument("key", type=str)
def delete(key: str) -> None:
    """Delete a variable"""
    try:
        store.delete(key)
        click.secho(f"Variable '{key}' deleted", fg="green")
        # Note: IDE bindings are automatically updated in the background
    except KeyError:
        click.secho(f"Variable '{key}' not found", fg="red")




@vars.command()
def generate_bindings() -> None:
    """Manually generate/refresh IDE support files (normally done automatically)"""
    from pathlib import Path
    from scriptthing.vars import _generate_stub_file
    
    try:
        # Generate stub file for IDE support (.pyi)
        stub_content = _generate_stub_file()
        stub_file = Path(__file__).parent.parent / "vars.pyi"
        
        with stub_file.open("w") as f:
            f.write(stub_content)
        
        click.secho(f"✓ IDE stub file generated: {stub_file}", fg="green")
        
        # Summary
        click.secho(f"\n🎉 IDE support file generated successfully!", fg="green", bold=True)
        click.secho("Your IDE should now detect variables for autocompletion.", fg="blue")
        click.secho("\n💡 Note: This file is automatically updated when you add/modify variables.", fg="blue")
        click.secho("    You only need to run this command if auto-generation is disabled.", fg="blue")
        click.secho("\nUsage:", fg="yellow")
        click.secho("  from scriptthing.vars import VARIABLE_NAME", fg="cyan")
        click.secho("  # Variables are accessed dynamically via __getattr__", fg="cyan")
        
    except Exception as e:
        click.secho(f"✗ IDE stub file generation failed: {e}", fg="red")


@vars.command()
@click.argument("enabled", type=click.Choice(["on", "off", "status"]))
def auto_bindings(enabled: str) -> None:
    """Control automatic IDE binding generation (on/off/status)"""
    from pathlib import Path
    from scriptthing.config.config import get_scriptthing_home, get_auto_generate_bindings
    
    config_file = get_scriptthing_home() / "config.toml"
    
    if enabled == "status":
        current_status = get_auto_generate_bindings()
        status_text = "enabled" if current_status else "disabled"
        click.secho(f"Automatic IDE binding generation is {status_text}", fg="blue")
        if current_status:
            click.secho("IDE stub file is automatically updated when variables change.", fg="green")
        else:
            click.secho("Use 'scriptthing vars generate-bindings' to manually update IDE stub file.", fg="yellow")
        return
    
    # Read current config
    try:
        if config_file.exists():
            content = config_file.read_text()
        else:
            # Create basic config if it doesn't exist
            config_file.parent.mkdir(exist_ok=True, parents=True)
            content = "[scriptthing]\n"
        
        # Update the auto_generate_bindings setting
        new_value = "true" if enabled == "on" else "false"
        
        if "auto_generate_bindings" in content:
            # Replace existing setting
            import re
            content = re.sub(
                r"auto_generate_bindings\s*=\s*\w+",
                f"auto_generate_bindings = {new_value}",
                content
            )
        else:
            # Add new setting
            if "[scriptthing]" in content:
                content = content.replace(
                    "[scriptthing]",
                    f"[scriptthing]\nauto_generate_bindings = {new_value}"
                )
            else:
                content += f"\n[scriptthing]\nauto_generate_bindings = {new_value}\n"
        
        # Write updated config
        config_file.write_text(content)
        
        action = "enabled" if enabled == "on" else "disabled"
        click.secho(f"Automatic IDE binding generation {action}", fg="green")
        
        if enabled == "on":
            click.secho("IDE stub file will be automatically updated when variables change.", fg="blue")
            # Trigger immediate generation
            from scriptthing.vars import _auto_generate_bindings_if_enabled
            _auto_generate_bindings_if_enabled()
            click.secho("Generated current IDE stub file.", fg="green")
        else:
            click.secho("Use 'scriptthing vars generate-bindings' to manually update IDE stub file.", fg="yellow")
            
    except Exception as e:
        click.secho(f"Error updating config: {e}", fg="red")


# Function to register the vars command group
def register_vars_commands(cli_group: click.Group) -> None:
    """Register vars commands with the main CLI group"""
    cli_group.add_command(vars)