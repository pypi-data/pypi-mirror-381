import click
from pathlib import Path
from typing import Optional

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
    refresh_repo(repo)
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
def refresh(path: Optional[str]) -> None:
    from scriptthing.repo import discover_repo
    if path:
        repo = register_repo(Path(path))
        refresh_repo(repo)
        Print.confirm(f"Refreshed repo '{repo.name}'")
    else:
        for r in list_registered_repos():
            refresh_repo(r)
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


@repos.command("install-explicit")
@click.option("--repo", "repo_spec", help="Repo name or path")
def install_explicit(repo_spec: str | None) -> None:
    """Install explicit per-script requirements (from '# requires:' comments) across repo scripts."""
    repo = resolve_repo(repo_spec)
    from scriptthing.templating.paths import list_scripts
    from scriptthing.compiler import compile_script
    installed = set()
    for link in list_scripts():
        # Only consider scripts from this repo's bin
        try:
            if link.resolve().is_relative_to(repo.root):
                script_path = link.resolve()
            else:
                continue
        except Exception:
            continue
        try:
            _, ctx = compile_script(script_path)
            reqs = ctx.get('requirements')
            if reqs and isinstance(reqs, dict):
                for req in (reqs.get('explicit') or []):
                    if req in installed:
                        continue
                    installed.add(req)
                    python_bin, _ = ensure_repo_venv(repo.root)
                    if python_bin.exists():
                        ensure_pip_in_venv(python_bin)
                        subprocess.run([str(python_bin), '-m', 'pip', 'install', req], cwd=str(repo.root))
        except Exception:
            continue
    Print.confirm(f"Installed {len(installed)} explicit requirements")


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
    for d in [dest/"scripts", dest/"functions", dest/"bin", dest/"modules"]:
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
    refresh_repo(repo)
    Print.confirm(f"Created and registered repo '{repo.name}' at {dest}")


# Register with main CLI
def register_repo_commands(cli_group: click.Group) -> None:
    cli_group.add_command(repos)

