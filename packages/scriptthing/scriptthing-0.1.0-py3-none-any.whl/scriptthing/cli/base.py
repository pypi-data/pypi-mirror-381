import click
from typing import Any
from scriptthing.config.config import get_or_create_config
from scriptthing.templating.paths import generate_shell_install_script
from scriptthing.repo import list_registered_repos, ensure_default_repo
from scriptthing.repo import ensure_default_repo


@click.group()
def cli() -> None:
    """scriptthing - A tool for managing and running scripts"""
    # Ensure default repo exists and is registered
    try:
        ensure_default_repo()
    except Exception:
        pass


@cli.command()
def config() -> None:
    """Show current configuration"""
    _config: Any = get_or_create_config()
    click.echo(_config)


@cli.command()
@click.option("--help-text", is_flag=True, help="Show instructions for adding to shell startup")
def install(help_text: bool) -> None:
    """Output shell code to source all functions"""
    if help_text:
        click.echo("Add this line to your ~/.bashrc or ~/.zshrc:")
        click.echo('eval "$(scriptthing install)"')
        return
    
    # Export repo bins on PATH based on repo config
    lines = []
    try:
        repos = list_registered_repos()
        # Include default repo first
        try:
            default_repo = ensure_default_repo()
            repos = [default_repo] + [r for r in repos if r.root != default_repo.root]
        except Exception:
            pass
        for r in repos:
            if getattr(r, 'add_bin_to_path', True) and r.bin_dir.exists():
                lines.append(f'export PATH="{r.bin_dir}:$PATH"')
    except Exception:
        pass
    lines.append(generate_shell_install_script())
    click.echo("\n".join(lines))