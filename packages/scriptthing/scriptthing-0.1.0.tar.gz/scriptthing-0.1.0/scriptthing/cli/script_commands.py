import click
from typing import Any
from pathlib import Path
from scriptthing.repo import list_registered_repos, refresh_repo, resolve_repo, ensure_default_repo
from scriptthing.templating.lang import languages
from scriptthing.templating.paths import (
    create_script_in_language, 
    list_scripts, 
    delete_script, 
    get_script_by_name,
    list_scripts_with_repos,
    set_script_permissions,
    get_script_names,
)
from scriptthing.shell import open_editor
from scriptthing.utils.pretty import Print
from shutil import copy


@click.command()
@click.option("--edit/--no-edit", type=bool, default=True)
@click.option("--repo", "repo_spec", help="Repo name or path to create in")
@click.argument("language", type=click.Choice(languages.keys()))
@click.argument("name", type=str)
def new(language: str, name: str, edit: bool, repo_spec: str | None) -> None:
    """Create a new script in the specified language"""
    try:
        # Create inside resolved repo (explicit, DEFAULT_REPO var, or default)
        repo = resolve_repo(repo_spec)
        if language == 'function':
            target_dir = repo.functions_dir
        elif language == 'extension':
            target_dir = repo.extensions_dir
        else:
            target_dir = repo.scripts_dir
        p: Path = create_script_in_language(language, name, _bin=target_dir)
        Print.confirm(p)
        if edit:
            open_editor(p)
        # If there are registered repos, refresh symlinks in case user's default location is inside a repo
        for r in list_registered_repos():
            try:
                refresh_repo(r)
            except Exception:
                pass
    except ValueError as ex:
        Print.red(ex.args[0])


@click.command()
@click.option("--repo", "repo_spec", help="Repo name or path to select when ambiguous")
@click.argument("name", type=str)
def edit(name: str, repo_spec: str | None) -> None:
    """Edit an existing script, function, or extension"""
    # Try direct lookup across symlink bin, functions, and extensions
    _script: Path | None = get_script_by_name(name)
    if _script is None:
        # Resolve repo and try with common extensions
        repo = resolve_repo(repo_spec)
        candidates = [
            repo.scripts_dir / name,
            repo.scripts_dir / f"{name}.py",
            repo.scripts_dir / f"{name}.sh",
            repo.functions_dir / f"{name}.sh",
            repo.extensions_dir / f"{name}.sh",
        ]
        _script = next((p for p in candidates if p.exists()), None)
    if _script:
        # Ensure editor opens the actual file with extension if it's a script in a repo
        open_editor(_script)
    else:
        Print.red(f"Script, function, or extension '{name}' not found")


@click.command()
@click.argument("name", type=click.Choice(get_script_names()))
def rm(name: str) -> None:
    """Remove a script, function, or extension"""
    delete_script(name)


@click.command()
def ls() -> None:
    """List all scripts, functions, and extensions"""
    items = list_scripts_with_repos()
    if not items:
        Print.info("No scripts, functions, or extensions found")
        return
    
    for item in items:
        is_function = item.path.parent.name == "functions" and item.path.suffix == ".sh"
        is_extension = item.path.parent.name == "extensions" and item.path.suffix == ".sh"
        name = item.path.stem if (is_function or is_extension) else item.path.name
        if is_function:
            type_label = "function"
        elif is_extension:
            type_label = "extension"
        else:
            type_label = "script"
        
        if item.repo_name:
            Print.info(f"{name} ({type_label}) [repo: {item.repo_name}]")
        else:
            Print.info(f"{name} ({type_label}) [global]")


@click.command()
@click.argument("name", type=click.Choice(get_script_names()))
def compile(name: str) -> None:
    """Show the compiled version of a script"""
    from scriptthing.compiler import compile_script
    
    script: Path = get_script_by_name(name)
    if not script:
        Print.red(f"Script '{name}' not found")
        return
    
    try:
        compiled_content, analysis_context = compile_script(script)
        click.echo(compiled_content)
    except Exception as e:
        Print.red(f"Error compiling script: {e}")

@click.command("import")
@click.argument("path", type=click.Path())
@click.option("--repo", "repo_spec", help="Repo name or path to import into")
def _import(path, repo_spec: str | None = None):
    path = Path(path)
    repo = resolve_repo(repo_spec)
    # Determine destination under repo scripts preserving extension
    dest_name = path.name
    dest_path = repo.scripts_dir / dest_name
    copy(path, dest_path)
    set_script_permissions(dest_path)
    # Refresh symlinks
    try:
        refresh_repo(repo)
    except Exception:
        pass
    Print.confirm(f"imported script to {dest_path}")


# Function to register all script commands with the main CLI
def register_script_commands(cli_group: click.Group) -> None:
    """Register all script commands with the main CLI group"""
    cli_group.add_command(new)
    cli_group.add_command(edit)
    cli_group.add_command(rm)
    cli_group.add_command(ls)
    cli_group.add_command(compile)
    cli_group.add_command(_import)
