from pathlib import Path
import subprocess
import sys
import importlib.util
import tempfile
import os
from typing import List, Any, Optional, Union
from types import ModuleType
from ..compiler import compile_script
from ..repo import get_python_interpreter_for_script, get_repo_env_for_script, get_repo_for_path
from ..repo import ensure_repo_dependencies
from ..deps import ensure_repo_venv, ensure_pip_in_venv
from ..compiler.analyzers import AnalysisContext
from ..compiler.analyzers import AnalysisContext
from ..compiler.bash_magic import compile_bash_magic


def execute_script(script_path: Path) -> Union[subprocess.CompletedProcess[bytes], ModuleType]:
    script_args: List[str] = sys.argv[2:]
    
    # Compilation step: get compiled script content and analysis context
    compiled_content: str
    analysis_context: AnalysisContext
    compiled_content, analysis_context = compile_script(script_path)
    
    # Use analysis context from compilation (no need to re-analyze)
    detected_lang: Optional[str] = analysis_context.get('lang')
    
    # Handle bash parameter parsing and compilation for shell scripts
    if detected_lang == 'shell':
        # Try bash magic compilation
        bash_compiled = compile_bash_magic(analysis_context, script_args)
        
        if bash_compiled is not None:
            # Magic happened! Use compiled script with no additional args
            compiled_content = bash_compiled
            final_script_args = []
        else:
            # No magic needed, use original args
            final_script_args = script_args
    else:
        final_script_args = script_args
    
    # Ensure repo dependencies before execution (auto-manage venv/requirements)
    try:
        repo = get_repo_for_path(script_path)
        if repo:
            ensure_repo_dependencies(repo, install=True)
            # Install explicit per-script requirements if any
            reqs = analysis_context.get('requirements') if 'requirements' in analysis_context.metadata else None
            if reqs and isinstance(reqs, dict):
                explicit = reqs.get('explicit', []) or []
                if explicit:
                    python_bin, _ = ensure_repo_venv(repo.root)
                    for req in explicit:
                        try:
                            if python_bin.exists():
                                ensure_pip_in_venv(python_bin)
                                subprocess.run([str(python_bin), '-m', 'pip', 'install', req], cwd=str(repo.root))
                        except Exception:
                            pass
    except Exception:
        pass

    # Create temporary file with compiled content
    with tempfile.NamedTemporaryFile(mode='w', suffix=script_path.suffix, delete=False) as temp_file:
        temp_file.write(compiled_content)
        compiled_script_path: Path = Path(temp_file.name)
    
    # Make temp file executable if original was executable
    if os.access(script_path, os.X_OK):
        os.chmod(compiled_script_path, 0o755)
    
    if detected_lang == 'python':
        # If script belongs to a registered repo with a venv, execute using that interpreter
        repo_python = get_python_interpreter_for_script(script_path)
        if repo_python is not None:
            cmd: List[str] = [str(repo_python), str(compiled_script_path)] + final_script_args
            env = get_repo_env_for_script(script_path)
            return subprocess.run(cmd, env=env)
        return _execute_python_module(compiled_script_path, final_script_args)
    elif detected_lang == 'shell':
        cmd: List[str] = ['bash', str(compiled_script_path)] + final_script_args
        return subprocess.run(cmd)

    else:
        # For unknown languages, try to determine interpreter from file extension or default to python
        if compiled_script_path.suffix == '.py':
            return _execute_python_module(compiled_script_path, final_script_args)
        elif compiled_script_path.suffix in ['.sh', '.bash']:
            cmd = ['bash', str(compiled_script_path)] + final_script_args
            env = get_repo_env_for_script(script_path)
            return subprocess.run(cmd, env=env)

        else:
            # Default to python for scriptthing scripts (which typically don't have extensions)
            # Try repo python first
            repo_python = get_python_interpreter_for_script(script_path)
            if repo_python is not None:
                cmd = [str(repo_python), str(compiled_script_path)] + final_script_args
                env = get_repo_env_for_script(script_path)
                return subprocess.run(cmd, env=env)
            return _execute_python_module(compiled_script_path, final_script_args)


def _execute_python_module(script_path: Path, script_args: List[str]) -> ModuleType:
    sys.argv = [str(script_path)] + script_args
    
    # Ensure the script path is absolute to avoid issues with relative paths
    abs_script_path: Path = script_path.resolve()
    
    # Verify the file exists before attempting to create spec
    if not abs_script_path.exists():
        raise FileNotFoundError(f"Script file not found: {abs_script_path}")
    
    # For Python execution, ensure the file has a .py extension for proper module spec creation
    # This is needed because scriptthing scripts might not have .py extensions
    final_script_path: Path = abs_script_path
    if not abs_script_path.suffix == '.py':
        # Create a copy with .py extension for module spec creation
        import tempfile
        import shutil
        
        temp_dir: str = tempfile.mkdtemp()
        final_script_path = Path(temp_dir) / (abs_script_path.name + '.py')
        shutil.copy2(abs_script_path, final_script_path)
    
    try:
        spec: Optional[importlib.util.ModuleSpec] = importlib.util.spec_from_file_location("__main__", final_script_path)
        
        # Handle the case where spec_from_file_location returns None
        if spec is None:
            raise RuntimeError(f"Could not create module spec from file: {final_script_path}")
        
        # Verify the spec has a loader
        if spec.loader is None:
            raise RuntimeError(f"Module spec has no loader for file: {final_script_path}")
        
        try:
            module: ModuleType = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except FileNotFoundError as e:
            # More helpful error message for file not found during execution
            raise FileNotFoundError(f"Failed to execute module - file not found: {final_script_path}") from e
        except Exception as e:
            # Catch any other execution errors and provide context
            raise RuntimeError(f"Failed to execute module {final_script_path}: {e}") from e
    
    finally:
        # Clean up temporary file if we created one
        if final_script_path != abs_script_path:
            import shutil
            shutil.rmtree(final_script_path.parent, ignore_errors=True)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: scriptthing-run <script_path>", file=sys.stderr)
        sys.exit(1)
        
    script_path: Path = Path(sys.argv[1])
    
    # Ensure script path is absolute early to avoid path resolution issues
    if not script_path.is_absolute():
        script_path = script_path.resolve()
    
    try:
        result: Union[subprocess.CompletedProcess[bytes], ModuleType] = execute_script(script_path)
        if result and hasattr(result, 'returncode'):
            sys.exit(result.returncode)
    except Exception as e:
        print(f"Error executing script: {e}", file=sys.stderr)
        raise e
