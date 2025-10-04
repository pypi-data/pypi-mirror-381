"""
Dynamic bindings loader.

Supports:
- from scriptthing.bindings import <symbols>   -> default repo bindings
- from scriptthing.bindings.<namespace> import <symbols>  -> bindings for specific repo

The <namespace> is derived from the repo name (sanitized to a valid identifier).
"""

from types import ModuleType
from pathlib import Path
import importlib.util
import sys
import re


def _sanitize_namespace(name: str) -> str:
    # Convert to a valid python identifier-ish namespace
    ns = re.sub(r"[^0-9a-zA-Z_]", "_", name)
    if ns and ns[0].isdigit():
        ns = f"_{ns}"
    return ns


def _load_bindings_from_path(path: Path) -> ModuleType | None:
    if not path.exists():
        return None
    spec = importlib.util.spec_from_file_location(f"_st_bindings_{hash(path)}", path)
    if spec is None or spec.loader is None:
        return None
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)  # type: ignore[attr-defined]
        return mod
    except Exception:
        return None


def _install_namespace_submodule(parent_name: str, ns: str, mod: ModuleType) -> ModuleType:
    full_name = f"{parent_name}.{ns}"
    ns_mod = ModuleType(full_name)
    # Copy public attributes
    for k, v in vars(mod).items():
        if not k.startswith("_"):
            setattr(ns_mod, k, v)
    # __all__ if present
    if hasattr(mod, "__all__"):
        ns_mod.__all__ = list(getattr(mod, "__all__"))  # type: ignore[attr-defined]
    sys.modules[full_name] = ns_mod
    return ns_mod


def _load_all() -> None:
    try:
        from ..repo import list_registered_repos, resolve_repo
    except Exception:
        return

    parent_name = __name__

    # Load per-repo namespaces
    for repo in list_registered_repos():
        try:
            ns = _sanitize_namespace(repo.name)
            bindings_path = Path(repo.root) / "modules" / "bindings.py"
            mod = _load_bindings_from_path(bindings_path)
            if mod is not None:
                _install_namespace_submodule(parent_name, ns, mod)
        except Exception:
            continue

    # Load default repo into package namespace and also create alias submodule "default"
    try:
        default_repo = resolve_repo(None)
        default_bindings_path = Path(default_repo.root) / "modules" / "bindings.py"
        default_mod = _load_bindings_from_path(default_bindings_path)
        if default_mod is not None:
            # Inject into package globals for from scriptthing.bindings import ...
            g = globals()
            exported = []
            for k, v in vars(default_mod).items():
                if not k.startswith("_"):
                    g[k] = v
                    exported.append(k)
            g["__all__"] = exported
            # Also create scriptthing.bindings.default submodule
            _install_namespace_submodule(parent_name, "default", default_mod)
    except Exception:
        pass


_load_all()

