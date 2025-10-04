import click
from pathlib import Path
from typing import Optional
import os

from scriptthing.repo import (
    register_repo,
    list_registered_repos,
    remove_repo,
    refresh_repo,
    ensure_repo_dependencies,
    resolve_repo,
)
from scriptthing.utils.pretty import Print
from scriptthing.deps import ensure_repo_venv, ensure_pip_in_venv
import shutil
import sys
import importlib
import subprocess


@click.group()
def repos() -> None:
    """Manage user script repositories (symlinks and dependencies)."""
    pass


@repos.command("add")
@click.argument("path", type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option("--no-install", is_flag=True, help="Do not install dependencies on add")
def add_repo(path: str, no_install: bool) -> None:
    repo = register_repo(Path(path))
    ok, msgs = ensure_repo_dependencies(repo, install=not no_install)
    refresh_repo(repo, sync_dotfiles_flag=False)
    for m in msgs:
        Print.info(m)
    if ok:
        Print.confirm(f"Registered repo '{repo.name}' at {repo.root}")
    else:
        Print.red("Repo registered but dependencies may be missing")


@repos.command("ls")
def list_repos() -> None:
    repos = list_registered_repos()
    if not repos:
        Print.info("No repositories registered")
        return
    for r in repos:
        Print.info(f"{r.name}: {r.root}")


@repos.command("rm")
@click.argument("path", type=click.Path(exists=False))
def remove(path: str) -> None:
    remove_repo(Path(path))
    Print.confirm(f"Removed repo {path}")


@repos.command("refresh")
@click.argument("path", required=False)
@click.option("--sync-dotfiles", is_flag=True, help="Also sync dotfiles symlinks")
def refresh(path: Optional[str], sync_dotfiles: bool) -> None:
    if path:
        repo = register_repo(Path(path))
        refresh_repo(repo, sync_dotfiles_flag=sync_dotfiles)
        Print.confirm(f"Refreshed repo '{repo.name}'")
    else:
        for r in list_registered_repos():
            refresh_repo(r, sync_dotfiles_flag=sync_dotfiles)
        Print.confirm("Refreshed all repos")


@repos.command("deps")
@click.argument("path")
@click.option("--no-install", is_flag=True, help="Only check dependencies, don't install")
def deps(path: str, no_install: bool) -> None:
    from scriptthing.repo import discover_repo
    repo = register_repo(Path(path)) if Path(path).exists() else discover_repo(Path(path))
    if not repo:
        Print.red("Not a scriptthing repo")
        return
    ok, msgs = ensure_repo_dependencies(repo, install=not no_install)
    for m in msgs:
        Print.info(m)
    if ok:
        Print.confirm("Dependencies OK")
    else:
        Print.red("Dependencies missing or failed to install")



@repos.command("install")
@click.argument("git_url")
@click.option("--name", help="Custom name for the repo (defaults to extracted from URL)")
@click.option("--branch", help="Git branch to checkout (defaults to default branch)")
@click.option("--path", "target_path", type=click.Path(), help="Target directory path (defaults to ~/.config/scriptthing/repos/<name>)")
def install_remote(git_url: str, name: Optional[str], branch: Optional[str], target_path: Optional[str]) -> None:
    """Install a remote repository by cloning it and adding it to ScriptThing."""
    import tempfile
    import urllib.parse
    
    # Extract repo name from URL if not provided
    if not name:
        if git_url.endswith('.git'):
            git_url_clean = git_url[:-4]
        else:
            git_url_clean = git_url
        parsed = urllib.parse.urlparse(git_url_clean)
        if parsed.path:
            name = parsed.path.split('/')[-1]
        if not name:
            name = "remote-repo"
    
    # Determine target directory
    if not target_path:
        repos_dir = Path.home() / ".config" / "scriptthing" / "repos"
        target_path = repos_dir / name
    
    target_dir = Path(target_path).expanduser().resolve()
    
    # Check if target already exists
    if target_dir.exists() and any(target_dir.iterdir()):
        Print.red(f"Target directory {target_dir} already exists and is not empty")
        sys.exit(1)
    
    try:
        # Clone the repository
        Print.info(f"Cloning {git_url} to {target_dir}")
        cmd = ["git", "clone"]
        if branch:
            cmd.extend(["-b", branch])
        cmd.extend([git_url, str(target_dir)])
        
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # Add to ScriptThing
        Print.info("Adding repository to ScriptThing...")
        repo = register_repo(target_dir)
        ok, msgs = ensure_repo_dependencies(repo, install=True)
        refresh_repo(repo, sync_dotfiles_flag=False)
        
        for msg in msgs:
            Print.info(msg)
        
        if ok:
            Print.confirm(f"Successfully installed remote repo '{repo.name}' from {git_url}")
        else:
            Print.red("Repo installed but dependencies may be missing")
            
    except subprocess.CalledProcessError as e:
        Print.red(f"Failed to clone repository: {e.stderr}")
        sys.exit(1)
    except Exception as e:
        Print.red(f"Failed to install remote repository: {e}")
        sys.exit(1)


@repos.command("create")
@click.argument("path", type=click.Path())
@click.option("--name", help="Repo name to set in scriptthing.toml")
def create_repo(path: str, name: Optional[str]) -> None:
    """Create a new repo by copying the starter skeleton and register it."""
    dest = Path(path).expanduser().resolve()
    if dest.exists() and any(dest.iterdir()):
        Print.red(f"Destination {dest} already exists and is not empty")
        sys.exit(1)
    # Locate starter repo in package resources
    try:
        from importlib import resources
        with resources.as_file(resources.files('scriptthing.resources.starter_repo')) as src:
            shutil.copytree(src, dest)
    except Exception as e:
        Print.red(f"Failed to copy starter repo: {e}")
        sys.exit(1)

    # Ensure directory structure exists
    for d in [dest/"scripts", dest/"functions", dest/"bin", dest/"modules", dest/"dotfiles"]:
        d.mkdir(parents=True, exist_ok=True)

    # Optionally set name in scriptthing.toml
    try:
        cfg = dest/"scriptthing.toml"
        if cfg.exists() and name:
            txt = cfg.read_text()
            import re
            if re.search(r"^\s*name\s*=\s*\".*\"", txt, flags=re.MULTILINE):
                txt = re.sub(r"^\s*name\s*=\s*\".*\"", f"name = \"{name}\"", txt, flags=re.MULTILINE)
            else:
                txt = txt.replace("[repo]", f"[repo]\nname = \"{name}\"", 1)
            cfg.write_text(txt)
    except Exception:
        pass

    # Register, ensure deps, and refresh symlinks
    repo = register_repo(dest)
    ensure_repo_dependencies(repo, install=True)
    refresh_repo(repo, sync_dotfiles_flag=False)
    Print.confirm(f"Created and registered repo '{repo.name}' at {dest}")


@repos.command("edit")
@click.argument("repo_spec", required=False)
@click.option("--editor", help="Editor command to use (defaults to $EDITOR)")
def edit_repo(repo_spec: Optional[str], editor: Optional[str]) -> None:
    """Open the repo directory in an editor."""
    try:
        repo = resolve_repo(repo_spec)
    except ValueError as e:
        Print.red(str(e))
        sys.exit(1)
    
    # Determine editor command
    editor_cmd = editor or os.environ.get('EDITOR')
    if not editor_cmd:
        Print.red("No editor specified. Set EDITOR environment variable or use --editor option")
        sys.exit(1)
    
    # Open the repo directory in the editor
    try:
        Print.info(f"Opening repo '{repo.name}' at {repo.root} in {editor_cmd}")
        subprocess.run([editor_cmd, str(repo.root)], check=True)
    except subprocess.CalledProcessError as e:
        Print.red(f"Failed to open editor: {e}")
        sys.exit(1)
    except FileNotFoundError:
        Print.red(f"Editor command not found: {editor_cmd}")
        sys.exit(1)


# Register with main CLI
def register_repo_commands(cli_group: click.Group) -> None:
    cli_group.add_command(repos)

