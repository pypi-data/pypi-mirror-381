import click
from typing import Optional
from pathlib import Path
from scriptthing.repo import resolve_repo, install_module_top_level, uninstall_module_top_level, list_installed_top_level_modules, export_modules, unexport_modules, get_available_modules, export_all_repos, unexport_all_repos
from scriptthing.utils.pretty import Print


@click.group()
def modules() -> None:
    """Manage per-module top-level installs from repo modules."""
    pass


@modules.command("install")
@click.argument("module_name")
@click.option("--repo", "repo_spec", help="Repo name or path")
@click.option("--python", "python_exe", type=click.Path(exists=True, path_type=Path),
              help="Target Python executable or directory containing Python (default: repo's internal venv)")
@click.option("--all-repos", "all_repos", is_flag=True, help="Install from all registered repositories")
def install(module_name: str, repo_spec: Optional[str], python_exe: Optional[Path], all_repos: bool) -> None:
    """Install a module. By default installs to repo's internal venv, or to external Python if --python is specified."""
    if python_exe is None:
        # Use repo's internal venv (original behavior)
        if all_repos:
            Print.red("--all-repos not supported for internal venv installation")
            return
        
        repo = resolve_repo(repo_spec)
        ok = install_module_top_level(repo, module_name)
        if ok:
            Print.confirm(f"Installed top-level module '{module_name}' from {repo.root}/modules")
        else:
            Print.red("Failed to install module. Ensure it exists under repo modules and venv is present.")
    else:
        # Use external Python environment (export behavior)
        if all_repos:
            success, message = export_all_repos(python_exe, [module_name])
        else:
            repo = resolve_repo(repo_spec)
            success, message = export_modules(repo, python_exe, [module_name])
        
        if success:
            Print.confirm(message)
        else:
            Print.red(message)


@modules.command("uninstall")
@click.argument("module_name")
@click.option("--repo", "repo_spec", help="Repo name or path")
@click.option("--python", "python_exe", type=click.Path(exists=True, path_type=Path),
              help="Target Python executable or directory containing Python (default: repo's internal venv)")
@click.option("--all-repos", "all_repos", is_flag=True, help="Uninstall from all registered repositories")
def uninstall(module_name: str, repo_spec: Optional[str], python_exe: Optional[Path], all_repos: bool) -> None:
    """Uninstall a module. By default uninstalls from repo's internal venv, or from external Python if --python is specified."""
    if python_exe is None:
        # Use repo's internal venv (original behavior)
        if all_repos:
            Print.red("--all-repos not supported for internal venv uninstallation")
            return
        
        repo = resolve_repo(repo_spec)
        ok = uninstall_module_top_level(repo, module_name)
        if ok:
            Print.confirm(f"Uninstalled top-level module '{module_name}'")
        else:
            Print.red("Nothing to uninstall or mismatch with installed module.")
    else:
        # Use external Python environment (unexport behavior)
        if all_repos:
            success, message = unexport_all_repos(python_exe, [module_name])
        else:
            repo = resolve_repo(repo_spec)
            success, message = unexport_modules(repo, python_exe, [module_name])
        
        if success:
            Print.confirm(message)
        else:
            Print.red(message)


@modules.command("ls")
@click.option("--repo", "repo_spec", help="Repo name or path")
@click.option("--installed", "show_installed", is_flag=True, help="Show installed modules in repo's internal venv")
@click.option("--available", "show_available", is_flag=True, help="Show available modules in repository")
def list_modules(repo_spec: Optional[str], show_installed: bool, show_available: bool) -> None:
    """List modules. By default shows both installed and available modules."""
    repo = resolve_repo(repo_spec)
    
    # If no specific flags, show both
    if not show_installed and not show_available:
        show_installed = True
        show_available = True
    
    if show_installed:
        mods = list_installed_top_level_modules(repo)
        if not mods:
            Print.info("No top-level modules installed")
        else:
            Print.info("Installed modules:")
            for m in mods:
                Print.info(f"  {m}")
    
    if show_available:
        modules = get_available_modules(repo)
        if not modules:
            Print.info(f"No modules found in {repo.name}")
        else:
            Print.info(f"Available modules in {repo.name}:")
            for module in modules:
                Print.info(f"  {module}")






def register_modules_commands(cli_group: click.Group) -> None:
    cli_group.add_command(modules)

