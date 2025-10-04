import click
from typing import Optional
from pathlib import Path
from scriptthing.repo import resolve_repo, install_module_top_level, uninstall_module_top_level, list_installed_top_level_modules
from scriptthing.utils.pretty import Print


@click.group()
def modules() -> None:
    """Manage per-module top-level installs from repo modules."""
    pass


@modules.command("install")
@click.argument("module_name")
@click.option("--repo", "repo_spec", help="Repo name or path")
def install(module_name: str, repo_spec: Optional[str]) -> None:
    repo = resolve_repo(repo_spec)
    ok = install_module_top_level(repo, module_name)
    if ok:
        Print.confirm(f"Installed top-level module '{module_name}' from {repo.root}/modules")
    else:
        Print.red("Failed to install module. Ensure it exists under repo modules and venv is present.")


@modules.command("uninstall")
@click.argument("module_name")
@click.option("--repo", "repo_spec", help="Repo name or path")
def uninstall(module_name: str, repo_spec: Optional[str]) -> None:
    repo = resolve_repo(repo_spec)
    ok = uninstall_module_top_level(repo, module_name)
    if ok:
        Print.confirm(f"Uninstalled top-level module '{module_name}'")
    else:
        Print.red("Nothing to uninstall or mismatch with installed module.")


@modules.command("ls")
@click.option("--repo", "repo_spec", help="Repo name or path")
def list_installed(repo_spec: Optional[str]) -> None:
    repo = resolve_repo(repo_spec)
    mods = list_installed_top_level_modules(repo)
    if not mods:
        Print.info("No top-level modules installed")
        return
    for m in mods:
        Print.info(m)


def register_modules_commands(cli_group: click.Group) -> None:
    cli_group.add_command(modules)

