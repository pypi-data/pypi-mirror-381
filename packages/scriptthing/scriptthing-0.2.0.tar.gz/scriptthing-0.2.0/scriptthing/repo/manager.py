from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import time
import urllib.parse
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from pydantic import BaseModel, Field, field_validator

from ..config.config import get_scriptthing_home, get_or_create_functions_dir, get_or_create_extensions_dir
try:
    import tomllib as toml  # type: ignore
except Exception:  # pragma: no cover
    import toml  # type: ignore
from ..utils.pretty import Print
from ..deps import ensure_repo_venv, ensure_pip_in_venv, install_requirements_txt


REPO_TOML = "scriptthing.toml"


class ScriptRepo(BaseModel):
    """
    ScriptThing repository model with centralized file-finding logic.
    
    ⚠️  CRITICAL: Always use find_script() method for locating files.
    Never construct paths manually (e.g., repo.scripts_dir / "name.py").
    
    This ensures consistent search priority and maintainable code.
    """
    root: Path
    name: str
    scripts_dir: Path
    functions_dir: Path
    extensions_dir: Path
    bin_dir: Path
    dotfiles_dir: Path
    config_path: Optional[Path] = None
    python_requirements: Optional[Path] = None
    add_bin_to_path: bool = True

    @field_validator('root')
    @classmethod
    def validate_root_exists(cls, v: Path) -> Path:
        """Ensure the root directory exists"""
        if not v.exists():
            raise ValueError(f"Repository root directory does not exist: {v}")
        return v

    def find_script(self, name: str) -> Optional[Path]:
        """
        Find a script by name across all relevant directories in this repository.
        
        This method provides centralized file-finding logic for locating scripts,
        functions, extensions, and dotfiles within a ScriptThing repository. It
        searches through all relevant directories in a specific priority order to
        ensure consistent and predictable script resolution.
        
        Search Order:
        1. Scripts directory (with .py and .sh extensions)
        2. Functions directory (with .sh extension)  
        3. Extensions directory (with .sh extension)
        4. Modules directory (with .py extension)
        5. Dotfiles directory (with various extensions and dot prefix)
        6. Bin directory (symlinks without extensions)
        
        The method handles various file naming patterns:
        - Scripts: "name" -> "name.py" or "name.sh"
        - Functions: "name" -> "name.sh" 
        - Extensions: "name" -> "name.sh"
        - Modules: "name" -> "name.py"
        - Dotfiles: "name" -> ".name", "name.ext", ".name.ext"
        - Bin symlinks: "name" -> symlink to actual script
        
        Args:
            name (str): The name of the script to find. Can be with or without
                       file extensions. For dotfiles, can include or omit the
                       leading dot (e.g., "bashrc" or ".bashrc").
                       
        Returns:
            Optional[Path]: The full path to the script if found, None if no
                           matching script exists in any of the search directories.
                           
        Examples:
            >>> repo = ScriptRepo(...)
            >>> # Find a Python script
            >>> script = repo.find_script("my_script")
            >>> # Find a shell function  
            >>> func = repo.find_script("my_func")
            >>> # Find a dotfile
            >>> dotfile = repo.find_script("bashrc")  # or ".bashrc"
            >>> # Find a script with extension
            >>> script = repo.find_script("another_script")
            
        Note:
            The search is case-sensitive and follows the exact priority order
            listed above. If multiple files with the same name exist in different
            directories, the one in the higher-priority directory will be returned.
        """
        # First check for actual script files with extensions in scripts directory
        for ext in ['.py', '.sh']:
            script_path = self.scripts_dir / f"{name}{ext}"
            if script_path.exists():
                return script_path
        
        # Check functions directory
        func_path = self.functions_dir / f"{name}.sh"
        if func_path.exists():
            return func_path
            
        # Check extensions directory
        ext_path = self.extensions_dir / f"{name}.sh"
        if ext_path.exists():
            return ext_path
        
        # Check modules directory
        modules_dir = self.root / "modules"
        if modules_dir.exists():
            module_path = modules_dir / f"{name}.py"
            if module_path.exists():
                return module_path
        
        # Check dotfiles directory with various patterns
        if self.dotfiles_dir.exists():
            # Try with and without dot prefix
            dotfile_candidates = [
                self.dotfiles_dir / f".{name}",
                self.dotfiles_dir / name,
            ]
            
            # Add common extension candidates
            common_extensions = [
                '.toml', '.conf', '.config', '.yaml', '.yml', '.json', '.ini', 
                '.cfg', '.rc', '.env', '.properties', '.xml', '.plist'
            ]
            for ext in common_extensions:
                dotfile_candidates.extend([
                    self.dotfiles_dir / f".{name}{ext}",
                    self.dotfiles_dir / f"{name}{ext}",
                ])
            
            # Check candidates
            for candidate in dotfile_candidates:
                if candidate.exists():
                    return candidate
            
            # Try to find any file with the name as a prefix using rglob
            for dotfile_path in self.dotfiles_dir.rglob("*"):
                if dotfile_path.is_file():
                    # Check if the file name matches (with or without dot prefix)
                    file_stem = dotfile_path.stem
                    file_name = dotfile_path.name
                    if (file_stem == name or file_stem == f".{name}" or 
                        file_name == name or file_name == f".{name}"):
                        return dotfile_path
        
        # Finally check scripts in bin (symlinks without extensions)
        bin_path = self.bin_dir / name
        if bin_path.exists():
            return bin_path
        
        return None

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
                dotfiles_dir = parent / section.get("dotfiles_dir", "dotfiles")
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
                    dotfiles_dir=dotfiles_dir,
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
                dotfiles_dir=root / entry.get("dotfiles_dir", "dotfiles"),
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
                "dotfiles_dir": str(r.dotfiles_dir.relative_to(r.root)) if r.dotfiles_dir.is_relative_to(r.root) else str(r.dotfiles_dir),
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
    refresh_repo(repo, sync_dotfiles_flag=False)
    return repo


def remove_repo(path: Path) -> None:
    repos = list_registered_repos()
    repos = [r for r in repos if r.root != path.resolve()]
    _write_registry(repos)
    # Remove symlinks for this repo
    _remove_symlinks_for_repo(path.resolve())


def refresh_repo(repo: ScriptRepo, sync_dotfiles_flag: bool = False) -> None:
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
    
    # Sync dotfiles if requested
    if sync_dotfiles_flag and repo.dotfiles_dir.exists():
        try:
            sync_dotfiles(repo, interactive=False)
        except Exception as e:
            Print.red(f"Failed to sync dotfiles during refresh: {e}")


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
        "dotfiles_dir = \"dotfiles\"\n"
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
    (root / "dotfiles").mkdir(exist_ok=True)
    cfg = root / REPO_TOML
    if not cfg.exists():
        cfg.write_text(_default_repo_toml("default"))
    # Register and ensure deps
    repo = register_repo(root)
    ensure_repo_dependencies(repo, install=True)
    refresh_repo(repo, sync_dotfiles_flag=False)
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
        refresh_repo(repo, sync_dotfiles_flag=False)
        return repo
    except Exception:
        return None


# === Dotfiles management ===

@dataclass
class DotfileConflict:
    """Represents a conflict between multiple repos for the same dotfile."""
    home_path: Path
    current_owner: Optional[str]  # Repo name that currently owns the file
    conflicting_repos: List[Tuple[str, Path]]  # List of (repo_name, dotfile_path) that want to own this file
    conflict_type: str  # "existing_file", "existing_symlink", "multiple_repos"

@dataclass
class DotfileOwnership:
    """Tracks which repo owns which dotfile."""
    repo_name: str
    home_path: Path
    dotfile_path: Path
    timestamp: float


def _get_dotfiles_registry() -> Path:
    """Get the path to the dotfiles registry file."""
    return get_scriptthing_home() / "dotfiles_registry.json"


def _load_dotfiles_registry() -> Dict[str, DotfileOwnership]:
    """Load the dotfiles registry from disk."""
    registry_file = _get_dotfiles_registry()
    if not registry_file.exists():
        return {}
    
    try:
        data = json.loads(registry_file.read_text())
        registry = {}
        for home_path_str, ownership_data in data.items():
            registry[home_path_str] = DotfileOwnership(
                repo_name=ownership_data["repo_name"],
                home_path=Path(home_path_str),
                dotfile_path=Path(ownership_data["dotfile_path"]),
                timestamp=ownership_data["timestamp"]
            )
        return registry
    except Exception:
        return {}


def _save_dotfiles_registry(registry: Dict[str, DotfileOwnership]) -> None:
    """Save the dotfiles registry to disk."""
    registry_file = _get_dotfiles_registry()
    registry_file.parent.mkdir(parents=True, exist_ok=True)
    
    data = {}
    for home_path_str, ownership in registry.items():
        data[home_path_str] = {
            "repo_name": ownership.repo_name,
            "dotfile_path": str(ownership.dotfile_path),
            "timestamp": ownership.timestamp
        }
    
    registry_file.write_text(json.dumps(data, indent=2))


def _detect_dotfile_conflicts(repo: ScriptRepo, home_dir: Path) -> List[DotfileConflict]:
    """Detect conflicts for dotfiles from this repo."""
    conflicts = []
    registry = _load_dotfiles_registry()
    dotfiles_dir = repo.dotfiles_dir
    
    if not dotfiles_dir.exists():
        return conflicts
    
    # Walk through all files in dotfiles directory
    for dotfile_path in dotfiles_dir.rglob("*"):
        if not dotfile_path.is_file():
            continue
            
        # Calculate relative path from dotfiles directory
        try:
            rel_path = dotfile_path.relative_to(dotfiles_dir)
        except ValueError:
            continue
            
        home_target = home_dir / rel_path
        home_path_str = str(home_target)
        
        # Check if another repo already owns this file
        if home_path_str in registry:
            existing_owner = registry[home_path_str]
            if existing_owner.repo_name != repo.name:
                # Conflict: different repo owns this file
                conflicts.append(DotfileConflict(
                    home_path=home_target,
                    current_owner=existing_owner.repo_name,
                    conflicting_repos=[(repo.name, dotfile_path)],
                    conflict_type="multiple_repos"
                ))
        elif home_target.exists():
            # File exists but not tracked - could be existing file or symlink
            if home_target.is_symlink():
                conflict_type = "existing_symlink"
            else:
                conflict_type = "existing_file"
            
            conflicts.append(DotfileConflict(
                home_path=home_target,
                current_owner=None,
                conflicting_repos=[(repo.name, dotfile_path)],
                conflict_type=conflict_type
            ))
    
    return conflicts


def _resolve_dotfile_conflicts(conflicts: List[DotfileConflict], repo_name: str, interactive: bool = True) -> List[Tuple[bool, str]]:
    """Resolve dotfile conflicts interactively. Returns list of (success, message) tuples."""
    results = []
    
    for conflict in conflicts:
        if not interactive:
            results.append((False, f"Skipped {conflict.home_path.name} (conflict detected, use interactive mode to resolve)"))
            continue
        
        print(f"\n⚠️  Conflict detected for {conflict.home_path.name}:")
        
        if conflict.conflict_type == "multiple_repos":
            print(f"   Currently owned by: {conflict.current_owner}")
            print(f"   Requested by: {repo_name}")
            print("\nOptions:")
            print("  1. Keep current owner")
            print("  2. Transfer to new repo")
            print("  3. Skip this file")
        elif conflict.conflict_type == "existing_symlink":
            print(f"   Existing symlink points to: {conflict.home_path.resolve()}")
            print(f"   New repo wants to link to: {conflict.conflicting_repos[0][1]}")
            print("\nOptions:")
            print("  1. Replace existing symlink")
            print("  2. Skip this file")
        else:  # existing_file
            print(f"   Existing regular file: {conflict.home_path}")
            print(f"   New repo wants to link to: {conflict.conflicting_repos[0][1]}")
            print("\nOptions:")
            print("  1. Backup existing file and create symlink")
            print("  2. Skip this file")
        
        try:
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if conflict.conflict_type == "multiple_repos":
                if choice == "1":
                    results.append((False, f"Skipped {conflict.home_path.name} (kept current owner)"))
                elif choice == "2":
                    results.append((True, f"Transfer ownership to {repo_name}"))
                else:
                    results.append((False, f"Skipped {conflict.home_path.name} (user cancelled)"))
            else:
                if choice == "1":
                    results.append((True, f"Replace existing {conflict.conflict_type}"))
                else:
                    results.append((False, f"Skipped {conflict.home_path.name} (user cancelled)"))
                    
        except (EOFError, KeyboardInterrupt):
            results.append((False, f"Skipped {conflict.home_path.name} (interrupted)"))
    
    return results

def sync_dotfiles(repo: ScriptRepo, interactive: bool = True) -> Tuple[bool, List[str]]:
    """
    Sync dotfiles from repo's dotfiles directory to user's home directory.
    
    Args:
        repo: The repository containing dotfiles
        interactive: If True, ask for confirmation before overwriting files
    
    Returns:
        Tuple of (success, list of messages)
    """
    messages: List[str] = []
    success = True
    home_dir = Path.home()
    dotfiles_dir = repo.dotfiles_dir
    
    if not dotfiles_dir.exists():
        messages.append(f"No dotfiles directory found at {dotfiles_dir}")
        return True, messages
    
    # Detect conflicts first
    conflicts = _detect_dotfile_conflicts(repo, home_dir)
    if conflicts:
        messages.append(f"Detected {len(conflicts)} potential conflicts")
        conflict_results = _resolve_dotfile_conflicts(conflicts, repo.name, interactive)
        
        # Process conflict resolution results
        for conflict, (resolved, msg) in zip(conflicts, conflict_results):
            messages.append(f"Conflict resolution: {msg}")
            if not resolved:
                continue
            
            # If resolved, proceed with the sync for this file
            dotfile_path = conflict.conflicting_repos[0][1]
            rel_path = dotfile_path.relative_to(dotfiles_dir)
            result_success, result_messages = _process_dotfile_with_registry(
                dotfile_path, rel_path, home_dir, repo, interactive
            )
            messages.extend(result_messages)
            if not result_success:
                success = False
    
    # Process non-conflicting files
    registry = _load_dotfiles_registry()
    for dotfile_path in dotfiles_dir.rglob("*"):
        if not dotfile_path.is_file():
            continue
            
        # Calculate relative path from dotfiles directory
        try:
            rel_path = dotfile_path.relative_to(dotfiles_dir)
        except ValueError:
            continue
            
        home_target = home_dir / rel_path
        home_path_str = str(home_target)
        
        # Skip if this file was already processed as a conflict
        if any(str(conflict.home_path) == home_path_str for conflict in conflicts):
            continue
        
        # Process this dotfile
        result_success, result_messages = _process_dotfile_with_registry(
            dotfile_path, rel_path, home_dir, repo, interactive
        )
        messages.extend(result_messages)
        if not result_success:
            success = False
    
    # Add summary message
    summary_msg = f"Successfully synced dotfiles from {repo.name}" if success else f"Some dotfiles failed to sync from {repo.name}"
    messages.append(summary_msg)
    
    return success, messages


def _process_dotfile_with_registry(dotfile_path: Path, rel_path: Path, home_dir: Path, repo: ScriptRepo, interactive: bool) -> Tuple[bool, List[str]]:
    """Process a single dotfile for syncing with registry tracking."""
    messages: List[str] = []
    home_target = home_dir / rel_path
    
    # Ensure parent directory exists
    home_target.parent.mkdir(parents=True, exist_ok=True)
    
    # Handle existing target
    if home_target.exists():
        should_proceed = _handle_existing_target(home_target, dotfile_path, rel_path, interactive, messages)
        if not should_proceed:
            return True, messages  # Success (already handled or skipped)
    
    # Create symlink
    try:
        home_target.symlink_to(dotfile_path)
        messages.append(f"✓ Linked {rel_path}")
        
        # Update registry
        registry = _load_dotfiles_registry()
        registry[str(home_target)] = DotfileOwnership(
            repo_name=repo.name,
            home_path=home_target,
            dotfile_path=dotfile_path,
            timestamp=time.time()
        )
        _save_dotfiles_registry(registry)
        
        return True, messages
    except Exception as e:
        messages.append(f"✗ Failed to link {rel_path}: {e}")
        return False, messages


def _process_dotfile(dotfile_path: Path, rel_path: Path, home_dir: Path, interactive: bool) -> Tuple[bool, List[str]]:
    """Process a single dotfile for syncing."""
    messages: List[str] = []
    home_target = home_dir / rel_path
    
    # Ensure parent directory exists
    home_target.parent.mkdir(parents=True, exist_ok=True)
    
    # Handle existing target
    if home_target.exists():
        should_proceed = _handle_existing_target(home_target, dotfile_path, rel_path, interactive, messages)
        if not should_proceed:
            return True, messages  # Success (already handled or skipped)
    
    # Create symlink
    try:
        home_target.symlink_to(dotfile_path)
        messages.append(f"✓ Linked {rel_path}")
        return True, messages
    except Exception as e:
        messages.append(f"✗ Failed to link {rel_path}: {e}")
        return False, messages


def _handle_existing_target(home_target: Path, dotfile_path: Path, rel_path: Path, interactive: bool, messages: List[str]) -> bool:
    """Handle existing target file. Returns True if we should proceed with linking."""
    if home_target.is_symlink():
        return _handle_existing_symlink(home_target, dotfile_path, rel_path, messages)
    else:
        return _handle_existing_file(home_target, rel_path, interactive, messages)


def _handle_existing_symlink(home_target: Path, dotfile_path: Path, rel_path: Path, messages: List[str]) -> bool:
    """Handle existing symlink. Returns True if we should proceed with linking."""
    try:
        if home_target.resolve() == dotfile_path.resolve():
            messages.append(f"✓ {rel_path} already linked")
            return False  # Don't proceed, already correct
    except Exception:
        pass
    
    # Remove existing symlink
    home_target.unlink()
    messages.append(f"Removed existing symlink: {rel_path}")
    return True


def _handle_existing_file(home_target: Path, rel_path: Path, interactive: bool, messages: List[str]) -> bool:
    """Handle existing regular file. Returns True if we should proceed with linking."""
    if not interactive:
        messages.append(f"Skipped {rel_path} (already exists, use interactive mode to overwrite)")
        return False
    
    try:
        response = input(f"File {rel_path} already exists. Overwrite? [y/N]: ").strip().lower()
        if response not in ['y', 'yes']:
            messages.append(f"Skipped {rel_path} (user declined)")
            return False
    except (EOFError, KeyboardInterrupt):
        messages.append(f"Skipped {rel_path} (interrupted)")
        return False
    
    return True


def remove_dotfiles_symlinks(repo: ScriptRepo) -> Tuple[bool, List[str]]:
    """
    Remove dotfiles symlinks created by this repo from user's home directory.
    
    Args:
        repo: The repository whose dotfiles symlinks should be removed
    
    Returns:
        Tuple of (success, list of messages)
    """
    messages: List[str] = []
    success = True
    home_dir = Path.home()
    dotfiles_dir = repo.dotfiles_dir
    
    if not dotfiles_dir.exists():
        messages.append(f"No dotfiles directory found at {dotfiles_dir}")
        return True, messages
    
    # Walk through all files in dotfiles directory
    for dotfile_path in dotfiles_dir.rglob("*"):
        if not dotfile_path.is_file():
            continue
            
        # Calculate relative path from dotfiles directory
        try:
            rel_path = dotfile_path.relative_to(dotfiles_dir)
        except ValueError:
            continue
            
        # Process removal of this dotfile symlink
        result_success, result_messages = _remove_dotfile_symlink(dotfile_path, rel_path, home_dir)
        messages.extend(result_messages)
        if not result_success:
            success = False
    
    # Add summary message
    summary_msg = f"Successfully removed dotfiles symlinks from {repo.name}" if success else f"Some dotfiles symlinks failed to remove from {repo.name}"
    messages.append(summary_msg)
    
    return success, messages


def _remove_dotfile_symlink(dotfile_path: Path, rel_path: Path, home_dir: Path) -> Tuple[bool, List[str]]:
    """Remove a single dotfile symlink."""
    messages: List[str] = []
    home_target = home_dir / rel_path
    
    if not home_target.exists():
        messages.append(f"Skipped {rel_path} (doesn't exist)")
        return True, messages
    
    if not home_target.is_symlink():
        messages.append(f"Skipped {rel_path} (not a symlink)")
        return True, messages
    
    try:
        if home_target.resolve() == dotfile_path.resolve():
            home_target.unlink()
            messages.append(f"✓ Removed symlink: {rel_path}")
            return True, messages
        else:
            messages.append(f"Skipped {rel_path} (points to different file)")
            return True, messages
    except Exception as e:
        messages.append(f"✗ Failed to remove {rel_path}: {e}")
        return False, messages


def list_dotfiles_status(repo: ScriptRepo) -> List[str]:
    """
    List the status of dotfiles for a repository.
    
    Args:
        repo: The repository to check
    
    Returns:
        List of status messages
    """
    messages: List[str] = []
    home_dir = Path.home()
    dotfiles_dir = repo.dotfiles_dir
    
    if not dotfiles_dir.exists():
        messages.append(f"No dotfiles directory found at {dotfiles_dir}")
        return messages
    
    messages.append(f"Dotfiles status for {repo.name}:")
    
    # Walk through all files in dotfiles directory
    for dotfile_path in dotfiles_dir.rglob("*"):
        if not dotfile_path.is_file():
            continue
            
        # Calculate relative path from dotfiles directory
        try:
            rel_path = dotfile_path.relative_to(dotfiles_dir)
        except ValueError:
            continue
            
        # Get status for this dotfile
        status_msg = _get_dotfile_status(dotfile_path, rel_path, home_dir)
        messages.append(f"  {status_msg}")
    
    return messages


def _get_dotfile_status(dotfile_path: Path, rel_path: Path, home_dir: Path) -> str:
    """Get status message for a single dotfile."""
    home_target = home_dir / rel_path
    
    if not home_target.exists():
        return f"○ {rel_path} (not linked)"
    
    if not home_target.is_symlink():
        return f"✗ {rel_path} (file exists but not linked)"
    
    try:
        if home_target.resolve() == dotfile_path.resolve():
            return f"✓ {rel_path} (linked)"
        else:
            return f"⚠ {rel_path} (symlink to different file)"
    except Exception:
        return f"? {rel_path} (symlink status unclear)"


def hotswap_dotfile(home_path: Path, target_repo_name: str) -> Tuple[bool, List[str]]:
    """
    Hotswap a dotfile to point to a different repo's version.
    
    Args:
        home_path: The path in the home directory to hotswap
        target_repo_name: The repo to swap to
    
    Returns:
        Tuple of (success, list of messages)
    """
    messages: List[str] = []
    registry = _load_dotfiles_registry()
    home_path_str = str(home_path)
    
    if home_path_str not in registry:
        messages.append(f"File {home_path.name} is not tracked by ScriptThing")
        return False, messages
    
    current_ownership = registry[home_path_str]
    if current_ownership.repo_name == target_repo_name:
        messages.append(f"File {home_path.name} is already owned by {target_repo_name}")
        return True, messages
    
    # Find the target repo
    target_repo = None
    for repo in list_registered_repos():
        if repo.name == target_repo_name:
            target_repo = repo
            break
    
    if not target_repo:
        messages.append(f"Repository '{target_repo_name}' not found")
        return False, messages
    
    # Find the corresponding file in the target repo
    rel_path = home_path.relative_to(Path.home())
    target_dotfile_path = target_repo.dotfiles_dir / rel_path
    
    if not target_dotfile_path.exists():
        messages.append(f"File {rel_path} not found in repository '{target_repo_name}'")
        return False, messages
    
    # Backup current symlink target if needed
    backup_path = None
    if home_path.is_symlink():
        try:
            current_target = home_path.resolve()
            backup_path = current_target.parent / f"{current_target.name}.backup.{int(time.time())}"
            shutil.copy2(current_target, backup_path)
            messages.append(f"Backed up current file to {backup_path.name}")
        except Exception as e:
            messages.append(f"Warning: Could not backup current file: {e}")
    
    # Remove current symlink
    try:
        home_path.unlink()
    except Exception as e:
        messages.append(f"Failed to remove current symlink: {e}")
        return False, messages
    
    # Create new symlink
    try:
        home_path.symlink_to(target_dotfile_path)
        messages.append(f"✓ Swapped {home_path.name} to {target_repo_name}")
        
        # Update registry
        registry[home_path_str] = DotfileOwnership(
            repo_name=target_repo_name,
            home_path=home_path,
            dotfile_path=target_dotfile_path,
            timestamp=time.time()
        )
        _save_dotfiles_registry(registry)
        
        return True, messages
    except Exception as e:
        messages.append(f"✗ Failed to create new symlink: {e}")
        return False, messages


def list_available_dotfile_versions(home_path: Path) -> List[Tuple[str, Path]]:
    """
    List all available versions of a dotfile across repositories.
    
    Args:
        home_path: The path in the home directory
    
    Returns:
        List of (repo_name, dotfile_path) tuples
    """
    available_versions = []
    
    try:
        rel_path = home_path.relative_to(Path.home())
    except ValueError:
        # If the path is not relative to home, try to find it by name
        file_name = home_path.name
        for repo in list_registered_repos():
            if not repo.dotfiles_dir.exists():
                continue
                
            # Search for files with the same name
            for dotfile_path in repo.dotfiles_dir.rglob("*"):
                if dotfile_path.is_file() and dotfile_path.name == file_name:
                    available_versions.append((repo.name, dotfile_path))
        return available_versions
    
    for repo in list_registered_repos():
        if not repo.dotfiles_dir.exists():
            continue
            
        dotfile_path = repo.dotfiles_dir / rel_path
        if dotfile_path.exists():
            available_versions.append((repo.name, dotfile_path))
    
    return available_versions


def get_dotfile_ownership_info(home_path: Path) -> Optional[DotfileOwnership]:
    """Get ownership information for a dotfile."""
    registry = _load_dotfiles_registry()
    return registry.get(str(home_path))


# === External Python environment module export ===

def _find_python_in_directory(directory: Path) -> Optional[Path]:
    """
    Search for Python executable in a directory (e.g., virtual environment).
    
    Args:
        directory: Directory to search for Python executable
        
    Returns:
        Path to Python executable, or None if not found
    """
    if not directory.exists() or not directory.is_dir():
        return None
    
    # Common Python executable names and locations
    candidates = [
        directory / "bin" / "python",
        directory / "bin" / "python3",
        directory / "Scripts" / "python.exe",  # Windows
        directory / "Scripts" / "python3.exe",  # Windows
        directory / "python",
        directory / "python3",
    ]
    
    for candidate in candidates:
        if candidate.exists() and candidate.is_file():
            # Test if it's actually a Python executable
            try:
                result = subprocess.run(
                    [str(candidate), "--version"],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                if result.returncode == 0:
                    return candidate
            except (subprocess.TimeoutExpired, subprocess.CalledProcessError, FileNotFoundError, OSError):
                continue
    
    return None


def _get_site_packages_for_python(python_exe: Path) -> Optional[Path]:
    """
    Get the site-packages directory for a given Python executable.
    
    Args:
        python_exe: Path to the Python executable
        
    Returns:
        Path to the site-packages directory, or None if not found
    """
    try:
        # Use subprocess to get site-packages path reliably
        result = subprocess.run(
            [str(python_exe), "-c", "import sysconfig; print(sysconfig.get_path('purelib'))"],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            site_packages_path = Path(result.stdout.strip())
            if site_packages_path.exists():
                return site_packages_path
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError, FileNotFoundError, OSError):
        pass
    
    return None


def _resolve_python_executable(python_path: Path) -> Optional[Path]:
    """
    Resolve a Python executable from either a file path or directory.
    
    Args:
        python_path: Path to Python executable or directory containing Python
        
    Returns:
        Path to Python executable, or None if not found
    """
    if python_path.is_file():
        # Direct path to Python executable
        return python_path
    elif python_path.is_dir():
        # Directory - search for Python executable
        return _find_python_in_directory(python_path)
    else:
        return None


def export_modules(repo: ScriptRepo, python_exe: Path, module_names: Optional[List[str]] = None) -> Tuple[bool, str]:
    """
    Export a repository's modules to an external Python environment using a .pth file.
    
    Args:
        repo: The ScriptThing repository to export modules from
        python_exe: Path to the target Python executable or directory containing Python
        module_names: Optional list of specific module names to export. If None, exports all modules.
        
    Returns:
        Tuple of (success, message)
    """
    try:
        # Resolve the Python executable
        resolved_python = _resolve_python_executable(python_exe)
        if resolved_python is None:
            return False, f"Could not find Python executable in {python_exe}"
        
        # Get the target site-packages directory
        site_packages = _get_site_packages_for_python(resolved_python)
        if site_packages is None:
            return False, f"Could not determine site-packages directory for {resolved_python}"
        
        # Ensure the repo's modules directory exists
        modules_dir = repo.root / "modules"
        modules_dir.mkdir(exist_ok=True)
        
        # If specific modules requested, validate they exist
        if module_names:
            missing_modules = []
            for module_name in module_names:
                # Check for both .py file and directory
                module_file = modules_dir / f"{module_name}.py"
                module_dir = modules_dir / module_name
                if not module_file.exists() and not module_dir.exists():
                    missing_modules.append(module_name)
            
            if missing_modules:
                return False, f"Modules not found in {repo.name}: {', '.join(missing_modules)}"
        
        # Create the .pth file name
        if module_names:
            # For specific modules, create individual .pth files
            results = []
            for module_name in module_names:
                pth_filename = f"_scriptthing_{repo.name}_{module_name}.pth"
                pth_path = site_packages / pth_filename
                
                # Check if already exists
                if pth_path.exists():
                    results.append(f"Module {module_name} already exported (file exists: {pth_path})")
                    continue
                
                # Find the actual module path (either .py file or directory)
                module_file = modules_dir / f"{module_name}.py"
                module_dir = modules_dir / module_name
                
                if module_file.exists():
                    # For .py files, create a symlink in site-packages
                    target_link = site_packages / f"{module_name}.py"
                    if target_link.exists() or target_link.is_symlink():
                        target_link.unlink(missing_ok=True)
                    target_link.symlink_to(module_file.absolute())
                    results.append(f"Successfully exported module {module_name} from {repo.name}")
                elif module_dir.exists():
                    # For directories, create a symlink in site-packages
                    target_link = site_packages / module_name
                    if target_link.exists() or target_link.is_symlink():
                        target_link.unlink(missing_ok=True)
                    target_link.symlink_to(module_dir.absolute())
                    results.append(f"Successfully exported module {module_name} from {repo.name}")
                else:
                    results.append(f"Module {module_name} not found")
                    continue
            
            return True, "; ".join(results)
        else:
            # Export all modules (original behavior)
            pth_filename = f"_scriptthing_{repo.name}_modules.pth"
            pth_path = site_packages / pth_filename
            
            # Check if already exists
            if pth_path.exists():
                return False, f"Modules already exported to {python_exe} (file exists: {pth_path})"
            
            # Write the .pth file with the absolute path to modules directory
            pth_path.write_text(str(modules_dir.absolute()) + "\n")
            
            return True, f"Successfully exported modules from {repo.name} to {python_exe}"
        
    except PermissionError:
        return False, f"Permission denied: cannot write to {site_packages}"
    except Exception as e:
        return False, f"Failed to export modules: {e}"


def unexport_modules(repo: ScriptRepo, python_exe: Path, module_names: Optional[List[str]] = None) -> Tuple[bool, str]:
    """
    Remove exported modules from an external Python environment by deleting the .pth file.
    
    Args:
        repo: The ScriptThing repository to unexport modules from
        python_exe: Path to the target Python executable or directory containing Python
        module_names: Optional list of specific module names to unexport. If None, unexports all modules.
        
    Returns:
        Tuple of (success, message)
    """
    try:
        # Resolve the Python executable
        resolved_python = _resolve_python_executable(python_exe)
        if resolved_python is None:
            return False, f"Could not find Python executable in {python_exe}"
        
        # Get the target site-packages directory
        site_packages = _get_site_packages_for_python(resolved_python)
        if site_packages is None:
            return False, f"Could not determine site-packages directory for {resolved_python}"
        
        if module_names:
            # For specific modules, remove individual symlinks and .pth files
            results = []
            for module_name in module_names:
                # Check for both symlink and .pth file
                symlink_file = site_packages / f"{module_name}.py"
                symlink_dir = site_packages / module_name
                pth_filename = f"_scriptthing_{repo.name}_{module_name}.pth"
                pth_path = site_packages / pth_filename
                
                removed_any = False
                
                # Remove symlink files
                if symlink_file.exists() or symlink_file.is_symlink():
                    symlink_file.unlink()
                    results.append(f"Removed symlink for {module_name}.py")
                    removed_any = True
                
                # Remove symlink directories
                if symlink_dir.exists() or symlink_dir.is_symlink():
                    symlink_dir.unlink()
                    results.append(f"Removed symlink for {module_name} directory")
                    removed_any = True
                
                # Remove .pth file if it exists
                if pth_path.exists():
                    pth_path.unlink()
                    results.append(f"Removed .pth file for {module_name}")
                    removed_any = True
                
                if not removed_any:
                    results.append(f"Module {module_name} not exported (no files found)")
                else:
                    results.append(f"Successfully removed exported module {module_name} from {repo.name}")
            
            return True, "; ".join(results)
        else:
            # Remove all modules (original behavior)
            pth_filename = f"_scriptthing_{repo.name}_modules.pth"
            pth_path = site_packages / pth_filename
            
            # Check if file exists
            if not pth_path.exists():
                return False, f"Modules not exported to {python_exe} (file not found: {pth_path})"
            
            # Remove the .pth file
            pth_path.unlink()
            
            return True, f"Successfully removed exported modules from {repo.name} in {python_exe}"
        
    except PermissionError:
        return False, f"Permission denied: cannot remove from {site_packages}"
    except Exception as e:
        return False, f"Failed to unexport modules: {e}"


def get_available_modules(repo: ScriptRepo) -> List[str]:
    """
    Get list of available modules in a repository.
    
    Args:
        repo: The ScriptThing repository
        
    Returns:
        List of module names (files and directories in modules folder)
    """
    modules_dir = repo.root / "modules"
    if not modules_dir.exists():
        return []
    
    modules = []
    for item in modules_dir.iterdir():
        if item.is_file() and item.suffix == '.py':
            modules.append(item.stem)
        elif item.is_dir() and not item.name.startswith('.') and item.name != '__pycache__':
            modules.append(item.name)
    
    return sorted(modules)


def export_all_repos(python_exe: Path, module_names: Optional[List[str]] = None) -> Tuple[bool, str]:
    """
    Export modules from all registered repositories to an external Python environment.
    
    Args:
        python_exe: Path to the target Python executable or directory containing Python
        module_names: Optional list of specific module names to export. If None, exports all modules.
        
    Returns:
        Tuple of (success, message)
    """
    repos = list_registered_repos()
    if not repos:
        return False, "No registered repositories found"
    
    results = []
    success_count = 0
    
    for repo in repos:
        success, message = export_modules(repo, python_exe, module_names)
        if success:
            success_count += 1
        results.append(f"{repo.name}: {message}")
    
    if success_count == len(repos):
        return True, f"Successfully exported from all {len(repos)} repositories: " + "; ".join(results)
    elif success_count > 0:
        return False, f"Partial success: {success_count}/{len(repos)} repositories exported: " + "; ".join(results)
    else:
        return False, f"Failed to export from any repositories: " + "; ".join(results)


def unexport_all_repos(python_exe: Path, module_names: Optional[List[str]] = None) -> Tuple[bool, str]:
    """
    Remove exported modules from all registered repositories in an external Python environment.
    
    Args:
        python_exe: Path to the target Python executable or directory containing Python
        module_names: Optional list of specific module names to unexport. If None, unexports all modules.
        
    Returns:
        Tuple of (success, message)
    """
    repos = list_registered_repos()
    if not repos:
        return False, "No registered repositories found"
    
    results = []
    success_count = 0
    
    for repo in repos:
        success, message = unexport_modules(repo, python_exe, module_names)
        if success:
            success_count += 1
        results.append(f"{repo.name}: {message}")
    
    if success_count == len(repos):
        return True, f"Successfully unexported from all {len(repos)} repositories: " + "; ".join(results)
    elif success_count > 0:
        return False, f"Partial success: {success_count}/{len(repos)} repositories unexported: " + "; ".join(results)
    else:
        return False, f"Failed to unexport from any repositories: " + "; ".join(results)

