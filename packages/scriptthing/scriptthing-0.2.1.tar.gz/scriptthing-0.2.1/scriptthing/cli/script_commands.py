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
        elif language == 'module':
            target_dir = repo.root / "modules"
        else:
            target_dir = repo.scripts_dir
        p: Path = create_script_in_language(language, name, _bin=target_dir)
        Print.confirm(p)
        # Refresh symlinks immediately so script is available in bin before opening editor
        try:
            refresh_repo(repo)
        except Exception:
            pass
        # Also refresh other registered repos in case user's default location is inside a repo
        for r in list_registered_repos():
            try:
                refresh_repo(r)
            except Exception:
                pass
        if edit:
            open_editor(p, "auto")
    except ValueError as ex:
        Print.red(ex.args[0])


@click.command()
@click.option("--repo", "repo_spec", help="Repo name or path to select when ambiguous")
@click.option("--splits", "layout", flag_value="splits", help="Force horizontal splits for multiple files")
@click.option("--tabs", "layout", flag_value="tabs", help="Force tabs for multiple files")
@click.option("--standard", "layout", flag_value="standard", help="Use standard editor behavior (no special options)")
@click.argument("names", nargs=-1, required=True)
def edit(names: tuple[str, ...], repo_spec: str | None, layout: str | None) -> None:
    """Edit scripts with smart layouts.
    
    Opens scripts in your preferred editor with intelligent layout handling.
    Multiple files automatically use tabs (3+) or splits (2) unless overridden.
    
    Examples:
        st edit script1                    # Edit single script
        st edit script1 script2            # Edit 2 scripts in splits (auto)
        st edit script1 script2 script3    # Edit 3+ scripts in tabs (auto)
        st edit --splits script1 script2   # Force splits for 2+ files
        st edit --tabs script1 script2     # Force tabs for 2+ files
        st edit --standard script1 script2 # Use standard editor behavior
    """
    if not names:
        Print.red("No script names provided")
        return
    
    resolved_scripts = []
    missing_scripts = []
    
    for name in names:
        # Try direct lookup across symlink bin, functions, extensions, and dotfiles
        _script: Path | None = get_script_by_name(name)
        if _script is None:
            # Resolve repo and use centralized file-finding logic
            repo = resolve_repo(repo_spec)
            _script = repo.find_script(name)
        
        if _script:
            resolved_scripts.append(_script)
        else:
            missing_scripts.append(name)
    
    # Report missing scripts
    if missing_scripts:
        if len(missing_scripts) == 1:
            Print.red(f"Script, function, or extension '{missing_scripts[0]}' not found")
        else:
            Print.red(f"Scripts, functions, or extensions not found: {', '.join(missing_scripts)}")
    
    # Open editor with resolved scripts
    if resolved_scripts:
        # Use auto layout if no layout specified
        layout_mode = layout or "auto"
        if len(resolved_scripts) == 1:
            # Single file - use original behavior
            open_editor(resolved_scripts[0], layout_mode)
        else:
            # Multiple files - use new multi-file support
            open_editor(resolved_scripts, layout_mode)


@click.command()
@click.option("--repo", "repo_spec", help="Repo name or path to select when ambiguous")
@click.argument("name", type=str)
def rm(name: str, repo_spec: str | None) -> None:
    """Remove scripts from repositories.
    
    Deletes the specified script file from its repository.
    
    Examples:
        st rm script1                    # Remove single script
        st rm --repo myrepo script1      # Remove script from specific repo
    """
    try:
        # Try direct lookup across symlink bin, functions, extensions, and dotfiles
        script_path: Path | None = get_script_by_name(name)
        if script_path is None:
            # Resolve repo and use centralized file-finding logic
            repo = resolve_repo(repo_spec)
            script_path = repo.find_script(name)
        
        if script_path:
            script_path.unlink()
            Print.confirm(f"Removed {script_path}")
        else:
            Print.red(f"Script, function, or extension '{name}' not found")
    except ValueError as ex:
        Print.red(ex.args[0])


@click.command()
@click.option("--repo", "repo_spec", help="Repo name or path to select when ambiguous")
@click.argument("old_name", type=str)
@click.argument("new_name", type=str)
def mv(old_name: str, new_name: str, repo_spec: str | None) -> None:
    """Rename scripts within repositories.
    
    Renames a script file while preserving its location and refreshing symlinks.
    
    Examples:
        st mv old_script new_script              # Rename script
        st mv --repo myrepo old_script new_name  # Rename in specific repo
    """
    try:
        # Try direct lookup across symlink bin, functions, extensions, and dotfiles
        old_script_path: Path | None = get_script_by_name(old_name)
        if old_script_path is None:
            # Resolve repo and use centralized file-finding logic
            repo = resolve_repo(repo_spec)
            old_script_path = repo.find_script(old_name)
        
        if not old_script_path:
            Print.red(f"Script, function, or extension '{old_name}' not found")
            return
        
        # Determine new path in same directory, preserving extension if new_name doesn't have one
        old_parent = old_script_path.parent
        old_extension = old_script_path.suffix
        
        # If new_name has no extension and old file had one, preserve it
        if not Path(new_name).suffix and old_extension:
            new_script_path = old_parent / (new_name + old_extension)
        else:
            new_script_path = old_parent / new_name
        
        # Check if destination already exists
        if new_script_path.exists():
            Print.red(f"Destination '{new_script_path.name}' already exists")
            return
        
        # Rename the file
        old_script_path.rename(new_script_path)
        Print.confirm(f"Renamed {old_script_path.name} → {new_script_path.name}")
        
        # Refresh symlinks for all registered repos
        for repo in list_registered_repos():
            try:
                refresh_repo(repo)
            except Exception:
                pass
                
    except ValueError as ex:
        Print.red(ex.args[0])
    except Exception as ex:
        Print.red(f"Error renaming script: {ex}")


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
        is_dotfile = item.path.parent.name == "dotfiles" or "dotfiles" in item.path.parts
        
        if is_dotfile:
            # For dotfiles, show the relative path from dotfiles directory
            name = item.path.name
            type_label = "dotfile"
        elif is_function:
            name = item.path.stem
            type_label = "function"
        elif is_extension:
            name = item.path.stem
            type_label = "extension"
        else:
            name = item.path.name
            type_label = "script"
        
        if item.repo_name:
            Print.info(f"{name} ({type_label}) [repo: {item.repo_name}]")
        else:
            Print.info(f"{name} ({type_label}) [global]")



@click.command("import")
@click.argument("path", type=click.Path())
@click.option("--repo", "repo_spec", help="Repo name or path to import into")
def _import(path, repo_spec: str | None = None):
    """Import external scripts into repositories.
    
    Copies an external script file into a scriptthing repository and makes it
    available as a managed script with proper symlinks and permissions.
    
    Examples:
        st import ./my_tool.py                    # Import to default repo
        st import /path/to/script.sh              # Import absolute path
        st import tool.py --repo work-scripts     # Import to specific repo
        st import ../legacy/backup.py            # Import relative path
    
    The original file is preserved - only a copy is made. File permissions are
    automatically set to make the script executable.
    """
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
    cli_group.add_command(mv)
    cli_group.add_command(ls)
    cli_group.add_command(_import)
