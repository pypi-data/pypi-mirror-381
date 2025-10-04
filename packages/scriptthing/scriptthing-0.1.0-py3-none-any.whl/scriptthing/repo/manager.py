from __future__ import annotations

import json
import os
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from ..config.config import get_scriptthing_home, get_or_create_functions_dir, get_or_create_extensions_dir
try:
    import tomllib as toml  # type: ignore
except Exception:  # pragma: no cover
    import toml  # type: ignore
from ..utils.pretty import Print
from ..deps import ensure_repo_venv, ensure_pip_in_venv, install_requirements_txt


REPO_TOML = "scriptthing.toml"


@dataclass
class ScriptRepo:
    root: Path
    name: str
    scripts_dir: Path
    functions_dir: Path
    extensions_dir: Path
    bin_dir: Path
    config_path: Optional[Path]
    python_requirements: Optional[Path]
    add_bin_to_path: bool = True

    @staticmethod
    def discover(start: Path) -> Optional["ScriptRepo"]:
        current = start.resolve()
        for parent in [current] + list(current.parents):
            cfg = parent / REPO_TOML
            if cfg.exists():
                try:
                    conf = toml.loads(cfg.read_text())
                except Exception:
                    conf = {}
                section = conf.get("repo", conf)
                name = section.get("name", parent.name)
                scripts_dir = parent / section.get("scripts_dir", "scripts")
                functions_dir = parent / section.get("functions_dir", "functions")
                extensions_dir = parent / section.get("extensions_dir", "extensions")
                bin_dir = parent / section.get("bin_dir", "bin")
                add_bin_to_path = bool(section.get("add_bin_to_path", True))
                config_path: Optional[Path] = cfg
                python_requirements = parent / "requirements.txt"
                if not python_requirements.exists():
                    python_requirements = None
                return ScriptRepo(
                    root=parent,
                    name=name,
                    scripts_dir=scripts_dir,
                    functions_dir=functions_dir,
                    extensions_dir=extensions_dir,
                    bin_dir=bin_dir,
                    config_path=config_path,
                    python_requirements=python_requirements,
                    add_bin_to_path=add_bin_to_path,
                )
        return None


def discover_repo(path: Path) -> Optional[ScriptRepo]:
    return ScriptRepo.discover(path)


def _registry_file() -> Path:
    return get_scriptthing_home() / "repos.json"


def list_registered_repos() -> List[ScriptRepo]:
    reg = _registry_file()
    if not reg.exists():
        return []
    data = json.loads(reg.read_text())
    repos: List[ScriptRepo] = []
    for entry in data:
        root = Path(entry["root"]).expanduser()
        repos.append(
            ScriptRepo(
                root=root,
                name=entry.get("name", root.name),
                scripts_dir=root / entry.get("scripts_dir", "scripts"),
                functions_dir=root / entry.get("functions_dir", "functions"),
                extensions_dir=root / entry.get("extensions_dir", "extensions"),
                bin_dir=root / entry.get("bin_dir", "bin"),
                config_path=(root / entry["config_path"]) if entry.get("config_path") else None,
                python_requirements=(root / entry["python_requirements"]) if entry.get("python_requirements") else None,
                add_bin_to_path=bool(entry.get("add_bin_to_path", True)),
            )
        )
    return repos


def _write_registry(repos: List[ScriptRepo]) -> None:
    reg = _registry_file()
    reg.parent.mkdir(parents=True, exist_ok=True)
    data = []
    for r in repos:
        data.append(
            {
                "root": str(r.root),
                "name": r.name,
                "scripts_dir": str(r.scripts_dir.relative_to(r.root)) if r.scripts_dir.is_relative_to(r.root) else str(r.scripts_dir),
                "functions_dir": str(r.functions_dir.relative_to(r.root)) if r.functions_dir.is_relative_to(r.root) else str(r.functions_dir),
                "extensions_dir": str(r.extensions_dir.relative_to(r.root)) if r.extensions_dir.is_relative_to(r.root) else str(r.extensions_dir),
                "bin_dir": str(r.bin_dir.relative_to(r.root)) if r.bin_dir.is_relative_to(r.root) else str(r.bin_dir),
                "config_path": str(r.config_path.relative_to(r.root)) if r.config_path and r.config_path.is_relative_to(r.root) else (str(r.config_path) if r.config_path else None),
                "python_requirements": str(r.python_requirements.relative_to(r.root)) if r.python_requirements and r.python_requirements.is_relative_to(r.root) else (str(r.python_requirements) if r.python_requirements else None),
                "add_bin_to_path": r.add_bin_to_path,
            }
        )
    reg.write_text(json.dumps(data, indent=2))


def register_repo(path: Path) -> ScriptRepo:
    repo = discover_repo(path)
    if repo is None:
        # Create default TOML if none found
        cfg = path / REPO_TOML
        if not cfg.exists():
            cfg.write_text(_default_repo_toml(path.name))
        repo = discover_repo(path)
        if repo is None:
            raise ValueError("Unable to create or discover repository at path")

    repos = list_registered_repos()
    if any(r.root == repo.root for r in repos):
        return repo
    repos.append(repo)
    _write_registry(repos)
    refresh_repo(repo)
    return repo


def remove_repo(path: Path) -> None:
    repos = list_registered_repos()
    repos = [r for r in repos if r.root != path.resolve()]
    _write_registry(repos)
    # Remove symlinks for this repo
    _remove_symlinks_for_repo(path.resolve())


def refresh_repo(repo: ScriptRepo) -> None:
    """Create/update per-repo bin symlinks (bin -> scripts)."""
    # Ensure repo bin exists
    repo.bin_dir.mkdir(parents=True, exist_ok=True)

    # Create symlinks in repo bin pointing to scripts
    if repo.scripts_dir.exists():
        for script in repo.scripts_dir.glob("*"):
            if script.is_file() and not script.name.startswith('.'):
                link = repo.bin_dir / script.name
                # symlink shoud not have the suffix
                link = link.with_suffix('')
                _ensure_symlink(link, script)


def _ensure_symlink(link: Path, target: Path) -> None:
    try:
        if link.is_symlink() or link.exists():
            if link.is_symlink() and link.resolve() == target.resolve():
                return
            link.unlink()
        link.symlink_to(target)
        # Try to make target executable if it looks like a script
        try:
            mode = target.stat().st_mode
            target.chmod(mode | 0o755)
        except Exception:
            pass
    except Exception as e:
        Print.red(f"Failed to create symlink {link} -> {target}: {e}")


def _remove_symlinks_for_repo(repo_root: Path) -> None:
    # Only functions are global now; remove any function symlinks pointing into the repo
    functions_dir = get_or_create_functions_dir()
    for link in functions_dir.glob("*"):
        try:
            if link.is_symlink():
                tgt = link.resolve()
                if repo_root in tgt.parents:
                    link.unlink()
        except Exception:
            continue


def ensure_repo_dependencies(repo: ScriptRepo, install: bool = True) -> Tuple[bool, List[str]]:
    messages: List[str] = []
    ok = True

    # Python deps via venv
    venv_dir = repo.root / ".venv"
    python_bin = venv_dir / "bin" / "python"
    if install:
        messages.append("Creating virtual environment for repo")
        python_bin, venv_dir = ensure_repo_venv(repo.root)

    # Install requirements.txt if present and outdated
    if repo.python_requirements and repo.python_requirements.exists() and install:
        stamp = venv_dir / ".requirements_mtime"
        current_mtime = str(int(repo.python_requirements.stat().st_mtime))
        prev_mtime = stamp.read_text().strip() if stamp.exists() else None
        if prev_mtime != current_mtime:
            messages.append("Installing Python dependencies from requirements.txt")
            if python_bin.exists():
                install_requirements_txt(repo.root, repo.python_requirements)
            try:
                stamp.write_text(current_mtime)
            except Exception:
                pass

    # Install explicit per-script requirements collected from bindings/modules if requested later

    if not python_bin.exists():
        ok = False
        messages.append("Missing repo virtualenv; create .venv or add requirements.txt")

    # Ensure IDE/LSP visibility by adding repo/modules via .pth in venv site-packages
    try:
        sp = _get_repo_site_packages(repo)
        if sp is not None:
            pth = sp / "scriptthing_modules.pth"
            modules_dir = repo.root / "modules"
            modules_dir.mkdir(exist_ok=True)
            existing = pth.read_text().splitlines() if pth.exists() else []
            if str(modules_dir) not in existing:
                new_lines = [*existing, str(modules_dir)] if existing else [str(modules_dir)]
                pth.write_text("\n".join(new_lines) + "\n")
    except Exception:
        pass

    return ok, messages


def get_repo_for_path(path: Path) -> Optional[ScriptRepo]:
    path = path.resolve()
    for repo in list_registered_repos():
        if repo.root in path.parents or repo.root == path:
            return repo
    return None


def get_python_interpreter_for_script(script_path: Path) -> Optional[Path]:
    repo = get_repo_for_path(script_path)
    if not repo:
        return None
    venv_python = repo.root / ".venv" / "bin" / "python"
    if venv_python.exists():
        return venv_python
    return None


def get_repo_env_for_script(script_path: Path) -> Dict[str, str]:
    env = os.environ.copy()
    repo = get_repo_for_path(script_path)
    if not repo:
        return env
    # Prepend repo binaries if any
    local_bin = repo.root / "bin"
    if local_bin.exists():
        env["PATH"] = f"{local_bin}:{env.get('PATH','')}"
    # Activate venv env vars
    venv_dir = repo.root / ".venv"
    if venv_dir.exists():
        env["VIRTUAL_ENV"] = str(venv_dir)
        env["PATH"] = f"{venv_dir / 'bin'}:{env.get('PATH','')}"
        env.pop("PYTHONHOME", None)
    return env


def _default_repo_toml(name: str) -> str:
    return (
        "[repo]\n"
        f"name = \"{name}\"\n"
        "scripts_dir = \"scripts\"\n"
        "functions_dir = \"functions\"\n"
        "extensions_dir = \"extensions\"\n"
    )


def get_default_repo_root() -> Path:
    return get_scriptthing_home() / "repo"


def ensure_default_repo() -> ScriptRepo:
    root = get_default_repo_root()
    root.mkdir(parents=True, exist_ok=True)
    # Ensure structure
    (root / "scripts").mkdir(exist_ok=True)
    (root / "functions").mkdir(exist_ok=True)
    (root / "extensions").mkdir(exist_ok=True)
    cfg = root / REPO_TOML
    if not cfg.exists():
        cfg.write_text(_default_repo_toml("default"))
    # Register and ensure deps
    repo = register_repo(root)
    ensure_repo_dependencies(repo, install=True)
    refresh_repo(repo)
    return repo


# === Top-level module installation helpers ===
def _get_repo_site_packages(repo: ScriptRepo) -> Optional[Path]:
    """Resolve site-packages inside the repo's .venv."""
    venv = repo.root / ".venv"
    sp = venv / "lib"
    if not sp.exists():
        return None
    # Find first pythonX.Y dir
    for pyver in sp.iterdir():
        candidate = pyver / "site-packages"
        if candidate.exists():
            return candidate
    return None


def install_module_top_level(repo: ScriptRepo, module_name: str) -> bool:
    """Install a module/package from <repo>/modules/<module_name> into the repo venv site-packages via .pth or symlink.
    - If the target is a package dir, create a symlink into site-packages with the package name.
    - If the target is a single .py, create a symlink <name>.py into site-packages.
    Track in <repo>/.st/modules_installed.txt for uninstall.
    """
    modules_dir = repo.root / "modules"
    source_pkg = modules_dir / module_name
    if not source_pkg.exists():
        return False

    sp = _get_repo_site_packages(repo)
    if sp is None:
        return False

    sp.mkdir(parents=True, exist_ok=True)

    try:
        if source_pkg.is_dir():
            dest = sp / module_name
            if dest.exists() or dest.is_symlink():
                dest.unlink(missing_ok=True)
            dest.symlink_to(source_pkg)
        else:
            # single file
            if source_pkg.suffix != ".py":
                return False
            dest = sp / source_pkg.name
            if dest.exists() or dest.is_symlink():
                dest.unlink(missing_ok=True)
            dest.symlink_to(source_pkg)
        # Track
        track = repo.root / ".st" / "modules_installed.txt"
        track.parent.mkdir(parents=True, exist_ok=True)
        lines = []
        if track.exists():
            lines = track.read_text().splitlines()
        if module_name not in lines:
            lines.append(module_name)
        track.write_text("\n".join(lines) + "\n")
        return True
    except Exception:
        return False


def uninstall_module_top_level(repo: ScriptRepo, module_name: str) -> bool:
    modules_dir = repo.root / "modules"
    source_pkg = modules_dir / module_name
    sp = _get_repo_site_packages(repo)
    if sp is None:
        return False
    try:
        target_dir = sp / module_name
        target_file = sp / f"{module_name}.py"
        changed = False
        if target_dir.is_symlink() and target_dir.resolve() == source_pkg.resolve():
            target_dir.unlink()
            changed = True
        if target_file.is_symlink() and target_file.resolve() == source_pkg.resolve():
            target_file.unlink()
            changed = True
        # Update tracker
        track = repo.root / ".st" / "modules_installed.txt"
        if track.exists():
            lines = [l for l in track.read_text().splitlines() if l.strip() and l.strip() != module_name]
            track.write_text("\n".join(lines) + ("\n" if lines else ""))
        return changed
    except Exception:
        return False


def list_installed_top_level_modules(repo: ScriptRepo) -> List[str]:
    track = repo.root / ".st" / "modules_installed.txt"
    if not track.exists():
        return []
    return [l.strip() for l in track.read_text().splitlines() if l.strip()]


def find_repo_by_name(name: str) -> Optional[ScriptRepo]:
    for r in list_registered_repos():
        if r.name == name:
            return r
    return None


def resolve_repo(spec: Optional[str]) -> ScriptRepo:
    """Resolve a repository by name or path, or fallback to DEFAULT_REPO var, else default repo."""
    # If explicit spec provided
    if spec:
        p = Path(spec)
        if p.exists():
            # Ensure it's registered and refreshed
            repo = register_repo(p)
            return repo
        # Try by name
        repo = find_repo_by_name(spec)
        if repo:
            return repo
        # As a last attempt, try discovering upwards
        discovered = discover_repo(p)
        if discovered:
            register_repo(discovered.root)
            return discovered
        raise ValueError(f"Repo '{spec}' not found")

    # No explicit spec: check scriptthing var ST_DEFAULT_REPO
    try:
        from ..utils import store as _store
        default_spec = _store.get("ST_DEFAULT_REPO", None)
    except Exception:
        default_spec = None
    if default_spec:
        return resolve_repo(str(default_spec))

    # Fallback to global default repo
    return ensure_default_repo()


# pip bootstrap now lives in deps.manager.ensure_pip_in_venv


def install_internal_repo_if_needed() -> Optional[ScriptRepo]:
    try:
        # First check if internal repo is already registered
        existing_repo = find_repo_by_name("st-internal")
        if existing_repo:
            return existing_repo
        
        # If not registered, extract to persistent location and register
        from importlib import resources
        import shutil
        
        internal_repo_dir = get_scriptthing_home() / ".internal_repo"
        
        # Only extract if directory doesn't exist or is empty
        if not internal_repo_dir.exists() or not any(internal_repo_dir.iterdir()):
            # Clean up any existing partial extraction
            if internal_repo_dir.exists():
                shutil.rmtree(internal_repo_dir)
            
            # Extract resources to persistent location
            with resources.as_file(resources.files('scriptthing.resources.internal_repo')) as temp_path:
                shutil.copytree(temp_path, internal_repo_dir)
        
        # Register the persistent internal repo
        repo = register_repo(internal_repo_dir)
        refresh_repo(repo)
        return repo
    except Exception:
        return None

