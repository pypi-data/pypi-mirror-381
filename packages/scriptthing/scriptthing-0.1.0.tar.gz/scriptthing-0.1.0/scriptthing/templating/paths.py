import shutil
import stat
from pathlib import Path
from typing import List, Optional, NamedTuple
from ..config.config import get_or_create_functions_dir, get_or_create_extensions_dir
from ..repo import ensure_default_repo, list_registered_repos
from .lang import languages


class ScriptInfo(NamedTuple):
    """Information about a script including its repo"""
    path: Path
    repo_name: Optional[str]  # None for global functions/extensions


def set_script_permissions(script: Path) -> None:
    script.chmod(script.stat().st_mode | stat.S_IEXEC | stat.S_IREAD | stat.S_IWRITE)


def create_script_in_language(lang: str, name: str, _bin: Path = None) -> Path:
    template_path: Path = languages[lang]
    
    # Determine target directory and filename
    if lang == 'function':
        target_dir = _bin or get_or_create_functions_dir()
        script_filename = name if name.endswith('.sh') else f"{name}.sh"
        script_path = target_dir / script_filename
        exists_msg = f"A shell function called {name} already exists"
    elif lang == 'extension':
        target_dir = _bin or get_or_create_extensions_dir()
        script_filename = name if name.endswith('.sh') else f"{name}.sh"
        script_path = target_dir / script_filename
        exists_msg = f"A shell extension called {name} already exists"
    else:
        # Default target is the current repo scripts dir (caller passes _bin)
        # Fallback to default repo scripts dir
        if _bin is None:
            _bin = ensure_default_repo().scripts_dir
        target_dir = _bin
        if lang == 'py':
            script_filename = name if name.endswith('.py') else f"{name}.py"
        elif lang == 'sh':
            script_filename = name if name.endswith('.sh') else f"{name}.sh"
        else:
            script_filename = name
        script_path = target_dir / script_filename
        exists_msg = f"A script called {name} already exists"
    
    if script_path.exists():
        raise ValueError(exists_msg)
    
    # Create the file
    if lang == 'function':
        # For functions, replace placeholder with actual name
        content = template_path.read_text().replace("FUNCTION_NAME", name)
        script_path.write_text(content)
    elif lang == 'extension':
        # For extensions, just copy the template
        shutil.copy(template_path, script_path)
    else:
        # For scripts, copy template
        shutil.copy(template_path, script_path)
        set_script_permissions(script_path)
        

    
    return script_path


def list_scripts() -> List[Path]:
    """List all scripts and shell functions"""
    items = []
    
    # Regular scripts via per-repo bins
    for repo in list_registered_repos():
        if repo.bin_dir.exists():
            for file_path in repo.bin_dir.glob("*"):
                if file_path.is_file():
                    items.append(file_path)
        # Also include per-repo functions and extensions
        if repo.functions_dir.exists():
            items.extend(repo.functions_dir.glob("*.sh"))
        if repo.extensions_dir.exists():
            items.extend(repo.extensions_dir.glob("*.sh"))
    
    # Also include default repo
    try:
        default_repo = ensure_default_repo()
        if default_repo.bin_dir.exists():
            for file_path in default_repo.bin_dir.glob("*"):
                if file_path.is_file():
                    items.append(file_path)
        # Include default repo functions and extensions
        if default_repo.functions_dir.exists():
            items.extend(default_repo.functions_dir.glob("*.sh"))
        if default_repo.extensions_dir.exists():
            items.extend(default_repo.extensions_dir.glob("*.sh"))
    except Exception:
        pass
    
    # Shell functions: keep global functions dir for sourcing
    functions_dir = get_or_create_functions_dir()
    if functions_dir.exists():
        items.extend(functions_dir.glob("*.sh"))
    
    # Shell extensions: keep global extensions dir for sourcing
    extensions_dir = get_or_create_extensions_dir()
    if extensions_dir.exists():
        items.extend(extensions_dir.glob("*.sh"))
    
    return items


def list_scripts_with_repos() -> List[ScriptInfo]:
    """List all scripts and shell functions with their repo information"""
    items = []
    processed_repo_roots = set()
    
    # Regular scripts via per-repo bins
    for repo in list_registered_repos():
        processed_repo_roots.add(repo.root)
        if repo.bin_dir.exists():
            for file_path in repo.bin_dir.glob("*"):
                if file_path.is_file():
                    items.append(ScriptInfo(file_path, repo.name))
        # Also include per-repo functions and extensions
        if repo.functions_dir.exists():
            for file_path in repo.functions_dir.glob("*.sh"):
                items.append(ScriptInfo(file_path, repo.name))
        if repo.extensions_dir.exists():
            for file_path in repo.extensions_dir.glob("*.sh"):
                items.append(ScriptInfo(file_path, repo.name))
    
    # Also include default repo if not already processed
    try:
        default_repo = ensure_default_repo()
        if default_repo.root not in processed_repo_roots:
            if default_repo.bin_dir.exists():
                for file_path in default_repo.bin_dir.glob("*"):
                    if file_path.is_file():
                        items.append(ScriptInfo(file_path, default_repo.name))
            # Include default repo functions and extensions
            if default_repo.functions_dir.exists():
                for file_path in default_repo.functions_dir.glob("*.sh"):
                    items.append(ScriptInfo(file_path, default_repo.name))
            if default_repo.extensions_dir.exists():
                for file_path in default_repo.extensions_dir.glob("*.sh"):
                    items.append(ScriptInfo(file_path, default_repo.name))
    except Exception:
        pass
    
    # Shell functions: keep global functions dir for sourcing
    functions_dir = get_or_create_functions_dir()
    if functions_dir.exists():
        for file_path in functions_dir.glob("*.sh"):
            items.append(ScriptInfo(file_path, None))  # Global functions have no repo
    
    # Shell extensions: keep global extensions dir for sourcing
    extensions_dir = get_or_create_extensions_dir()
    if extensions_dir.exists():
        for file_path in extensions_dir.glob("*.sh"):
            items.append(ScriptInfo(file_path, None))  # Global extensions have no repo
    
    return items


def get_script_names() -> List[str]:
    """Get list of all script, function, and extension names"""
    names = []
    for item in list_scripts():
        if item.parent.name in ["functions", "extensions"] and item.suffix == ".sh":
            names.append(item.stem)  # Remove .sh for functions and extensions
        else:
            names.append(item.name)  # Keep full name for scripts
    return names


def resolve_script_to_actual_file(script_path: Path) -> Path:
    """
    Resolve a script path to the actual file with extension.
    If the path is a symlink in a bin directory, follow it to the target.
    Otherwise, return the path as-is.
    """
    if script_path.is_symlink():
        return script_path.resolve()
    return script_path


def get_script_by_name(name: str) -> Optional[Path]:
    """Get a script or shell function by name"""
    # Check per-repo bins, functions, and extensions
    for repo in list_registered_repos():
        # Check scripts in bin
        p = repo.bin_dir / name
        if p.exists():
            return p
        # Check functions
        func_p = repo.functions_dir / f"{name}.sh"
        if func_p.exists():
            return func_p
        # Check extensions
        ext_p = repo.extensions_dir / f"{name}.sh"
        if ext_p.exists():
            return ext_p
    
    try:
        default_repo = ensure_default_repo()
        # Check scripts in bin
        p = default_repo.bin_dir / name
        if p.exists():
            return p
        # Check functions
        func_p = default_repo.functions_dir / f"{name}.sh"
        if func_p.exists():
            return func_p
        # Check extensions
        ext_p = default_repo.extensions_dir / f"{name}.sh"
        if ext_p.exists():
            return ext_p
    except Exception:
        pass
    
    # Check global shell functions
    function_path = get_or_create_functions_dir() / f"{name}.sh"
    if function_path.exists():
        return function_path
    
    # Check global shell extensions
    extension_path = get_or_create_extensions_dir() / f"{name}.sh"
    if extension_path.exists():
        return extension_path
    
    return None


def _get_internal_script_by_name(name: str) -> Optional[Path]:
    # Internal scripts are exposed via internal repo now
    try:
        from ..repo import install_internal_repo_if_needed
        internal_repo = install_internal_repo_if_needed()
        if internal_repo:
            p = internal_repo.scripts_dir / name
            if p.exists():
                return p
    except Exception:
        pass
    return None


def delete_script(name: str) -> None:
    """Delete a script or shell function by name"""
    script_path = get_script_by_name(name)
    if script_path:
        script_path.unlink()
    else:
        raise ValueError(f"Script or function '{name}' not found")


def generate_shell_install_script() -> str:
    """Generate shell code that sources all shell extensions and provides function sourcing for bash scripts"""
    lines = ["# scriptthing shell setup"]
    
    # Always source extensions (available in all shells)
    extensions_dir = get_or_create_extensions_dir()
    extension_files = list(extensions_dir.glob("*.sh")) if extensions_dir.exists() else []
    
    # Also source per-repo extensions
    for repo in list_registered_repos():
        if repo.extensions_dir.exists():
            extension_files.extend(repo.extensions_dir.glob("*.sh"))
    
    # Include default repo extensions
    try:
        default_repo = ensure_default_repo()
        if default_repo.extensions_dir.exists():
            extension_files.extend(default_repo.extensions_dir.glob("*.sh"))
    except Exception:
        pass
    
    if extension_files:
        lines.append("# Shell extensions (always available)")
        lines.extend(f'source "{ext}"' for ext in extension_files)
    
    # Provide a function to source shell functions in bash scripts
    lines.append("")
    lines.append("# Function to source shell functions in bash scripts")
    lines.append("scriptthing_source_functions() {")
    
    functions_dir = get_or_create_functions_dir()
    function_files = list(functions_dir.glob("*.sh")) if functions_dir.exists() else []
    
    # Also include per-repo functions
    for repo in list_registered_repos():
        if repo.functions_dir.exists():
            function_files.extend(repo.functions_dir.glob("*.sh"))
    
    # Include default repo functions
    try:
        default_repo = ensure_default_repo()
        if default_repo.functions_dir.exists():
            function_files.extend(default_repo.functions_dir.glob("*.sh"))
    except Exception:
        pass
    
    if function_files:
        for func in function_files:
            lines.append(f'    source "{func}"')
    else:
        lines.append("    # No shell functions to source")
    
    lines.append("}")
    
    return "\n".join(lines)
