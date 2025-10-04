from .utils import store
from .utils import cli
from .utils import (
    read_args, argsclass,
    # Enhanced argsclass features
    Required, Positional, Flag, Counter, Hidden,
    Option, Argument, ArgumentConfig, ValidationError,
    FilePathArg, DirPathArg, PortArg, VerbosityArg
)

# Enable repo modules import path: scriptthing.modules -> <default-repo>/modules
try:
	import sys
	from pathlib import Path
	from .repo import ensure_default_repo
	_repo = ensure_default_repo()
	_modules = _repo.root / 'modules'
	if _modules.exists():
		# Add a virtual package path mapping: scriptthing.modules.*
		import importlib.util
		sys.path.append(str(_modules))
except Exception:
	pass
