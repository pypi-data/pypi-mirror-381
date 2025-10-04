import click
from pathlib import Path
from typing import Optional

from scriptthing.repo import (
    resolve_repo,
    sync_dotfiles,
    remove_dotfiles_symlinks,
    list_dotfiles_status,
    hotswap_dotfile,
    list_available_dotfile_versions,
    get_dotfile_ownership_info,
)
from scriptthing.utils.pretty import Print


@click.group("dotfiles")
def dotfiles() -> None:
    """Manage dotfiles for repositories."""
    pass


@dotfiles.command("sync")
@click.option("--repo", "repo_spec", help="Repo name or path")
@click.option("--no-interactive", is_flag=True, help="Don't ask for confirmation when overwriting files")
def dotfiles_sync(repo_spec: str | None, no_interactive: bool) -> None:
    """Create symlinks from repo dotfiles to home directory."""
    repo = resolve_repo(repo_spec)
    success, messages = sync_dotfiles(repo, interactive=not no_interactive)
    
    for msg in messages:
        Print.info(msg)
    
    if success:
        Print.confirm(f"Dotfiles synced for repo '{repo.name}'")
    else:
        Print.red(f"Some dotfiles failed to sync for repo '{repo.name}'")


@dotfiles.command("rm")
@click.option("--repo", "repo_spec", help="Repo name or path")
def dotfiles_rm(repo_spec: str | None) -> None:
    """Remove symlinks created by repo dotfiles."""
    repo = resolve_repo(repo_spec)
    success, messages = remove_dotfiles_symlinks(repo)
    
    for msg in messages:
        Print.info(msg)
    
    if success:
        Print.confirm(f"Dotfiles symlinks removed for repo '{repo.name}'")
    else:
        Print.red(f"Some dotfiles symlinks failed to remove for repo '{repo.name}'")


@dotfiles.command("status")
@click.option("--repo", "repo_spec", help="Repo name or path")
def dotfiles_status(repo_spec: str | None) -> None:
    """Show status of dotfiles symlinks."""
    repo = resolve_repo(repo_spec)
    messages = list_dotfiles_status(repo)
    
    for msg in messages:
        Print.info(msg)


@dotfiles.command("hotswap")
@click.argument("file_path", type=click.Path())
@click.argument("target_repo", type=str)
def dotfiles_hotswap(file_path: str, target_repo: str) -> None:
    """Hotswap a dotfile to point to a different repo's version."""
    home_path = Path(file_path).expanduser().resolve()
    
    if not home_path.exists():
        Print.red(f"File {file_path} does not exist")
        return
    
    success, messages = hotswap_dotfile(home_path, target_repo)
    
    for msg in messages:
        Print.info(msg)
    
    if success:
        Print.confirm(f"Successfully hotswapped {home_path.name} to {target_repo}")
    else:
        Print.red(f"Failed to hotswap {home_path.name}")


@dotfiles.command("versions")
@click.argument("file_path", type=click.Path())
def dotfiles_versions(file_path: str) -> None:
    """List all available versions of a dotfile across repositories."""
    home_path = Path(file_path).expanduser().resolve()
    
    # Get current ownership info
    ownership = get_dotfile_ownership_info(home_path)
    if ownership:
        Print.info(f"Current owner: {ownership.repo_name}")
        Print.info(f"Linked to: {ownership.dotfile_path}")
        Print.info("")
    
    # List available versions
    versions = list_available_dotfile_versions(home_path)
    
    if not versions:
        Print.info(f"No versions of {home_path.name} found in any repository")
        return
    
    Print.info(f"Available versions of {home_path.name}:")
    for repo_name, dotfile_path in versions:
        if ownership and ownership.repo_name == repo_name:
            Print.info(f"  ✓ {repo_name}: {dotfile_path} (current)")
        else:
            Print.info(f"  ○ {repo_name}: {dotfile_path}")


@dotfiles.command("conflicts")
@click.option("--repo", "repo_spec", help="Repo name or path")
def dotfiles_conflicts(repo_spec: str | None) -> None:
    """Check for potential conflicts with other repositories."""
    repo = resolve_repo(repo_spec)
    home_dir = Path.home()
    
    # Import the conflict detection function
    from scriptthing.repo.manager import _detect_dotfile_conflicts
    
    conflicts = _detect_dotfile_conflicts(repo, home_dir)
    
    if not conflicts:
        Print.confirm(f"No conflicts detected for repository '{repo.name}'")
        return
    
    Print.info(f"Detected {len(conflicts)} potential conflicts for repository '{repo.name}':")
    Print.info("")
    
    for conflict in conflicts:
        Print.info(f"⚠️  {conflict.home_path.name}:")
        if conflict.conflict_type == "multiple_repos":
            Print.info(f"   Currently owned by: {conflict.current_owner}")
            Print.info(f"   Requested by: {conflict.conflicting_repos[0][0]}")
        elif conflict.conflict_type == "existing_symlink":
            Print.info(f"   Existing symlink points to: {conflict.home_path.resolve()}")
            Print.info(f"   New repo wants to link to: {conflict.conflicting_repos[0][1]}")
        else:  # existing_file
            Print.info(f"   Existing regular file: {conflict.home_path}")
            Print.info(f"   New repo wants to link to: {conflict.conflicting_repos[0][1]}")
        Print.info("")




def register_dotfiles_commands(cli_group: click.Group) -> None:
    """Register dotfiles commands with the main CLI."""
    cli_group.add_command(dotfiles)
