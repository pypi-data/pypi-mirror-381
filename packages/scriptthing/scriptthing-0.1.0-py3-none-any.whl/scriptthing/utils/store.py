# Store persisent variables for use in scripts
import pickle
from datetime import datetime, timedelta
from typing import Any
from pathlib import Path


def __vars_path() -> Path:
    # Resolve repo-aware variables file under repo hidden directory
    try:
        from scriptthing.repo import resolve_repo
        repo = resolve_repo(None)
        st_dir = Path(repo.root) / ".st"
        st_dir.mkdir(parents=True, exist_ok=True)
        return st_dir/"vars.pickle"
    except Exception:
        # Fallback to legacy location to avoid breaking in constrained envs
        from scriptthing.config.config import get_scriptthing_home
        return get_scriptthing_home()/".__scriptthing_vars.pickle"

def __read_vars():
    _file = __vars_path()
    if not _file.exists():
        return {}
    with _file.open("rb") as f:
        vars = pickle.load(f)

    now = datetime.now()
    _vars = {k: v for k, v in vars.items()
            if v.get("ttl", None) is None or (v["created_at"] + v["ttl"]) >= now}
    if len(_vars) != len(vars):
        __write_vars(vars)

    return _vars

def __write_vars(vars):
    _file = __vars_path()
    with _file.open("wb") as f:
        pickle.dump(vars, f)


def put(key: str, value: Any, ttl: timedelta | None = None):
    vars = __read_vars()
    vars[key] = dict(value=value, created_at=datetime.now(), ttl=ttl)
    __write_vars(vars)
    
    # Auto-generate IDE bindings if enabled
    _trigger_auto_generation()

def delete(key: str):
    vars = __read_vars()
    del vars[key]
    __write_vars(vars)
    
    # Auto-generate IDE bindings if enabled
    _trigger_auto_generation()

    
def _get_all():
    return __read_vars()

NULL_VALUE = "NULL_VALUE_" + str(datetime.now().timestamp())

def get(key: str, default: Any = NULL_VALUE):
    vars_data = __read_vars()
    if key not in vars_data:
        if default == NULL_VALUE:
            raise KeyError(f"no value for variable {key}")
        return default
    
    return vars_data[key]["value"]


def _trigger_auto_generation():
    """
    Trigger automatic generation of IDE binding files.
    This is called after variables are modified and runs silently.
    """
    try:
        # Import here to avoid circular imports
        from ..vars import _auto_generate_bindings_if_enabled
        _auto_generate_bindings_if_enabled()
    except Exception:
        # Fail silently - don't break variable operations if binding generation fails
        pass


