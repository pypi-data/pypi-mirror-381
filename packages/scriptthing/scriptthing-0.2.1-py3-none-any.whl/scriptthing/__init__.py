from .utils import store
# CLI argument parsing utilities removed

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
