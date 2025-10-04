from collections.abc import Iterable
import shutil
import subprocess
from pathlib import Path
import json as _json
from dataclasses import dataclass
from typing import Union, List, Dict, Any
from ..formats import DataParser


@dataclass
class CompletedScriptResult(DataParser):
    """Script execution result with unified format parsing capabilities."""
    stdout: bytes
    stderr: bytes

    def __post_init__(self):
        """Initialize DataParser with stdout data."""
        super().__init__(self.stdout)

    @property
    def path(self) -> Path:
        """Get stdout as path."""
        return Path(self.text.strip())
    
    @property
    def stderr_text(self) -> str:
        """Get stderr as plain text."""
        return self.stderr.decode('utf-8') if self.stderr else ""
    



class Executable:
    def __init__(self, executable=None):
        """
        Initialize Executable with optional path.
        
        Args:
            executable: Either a Path object, script name string, or None.
                       If None, path will be determined from first argument in __call__.
                       If string, will lookup the script using get_script_by_name.
        """
        if executable is None:
            self._path = None
        elif isinstance(executable, str):
            # Import here to avoid circular imports
            from ..templating.paths import get_script_by_name
            script_path = get_script_by_name(executable)
            if script_path is None:
                raise FileNotFoundError(f"Script '{executable}' not found")
            self._path = script_path.absolute()
        else:
            # Assume it's a Path object
            self._path = executable.absolute()
    
    def __call__(self, *args, stdin_input=None, **kwargs) -> CompletedScriptResult:
        # Determine if it's a shell command or script execution
        first_arg = str(args[0]) if args else ""
        
        # Enhanced shell command detection
        shell_indicators = ['|', '>', '<', ';', '&&', '||', '$(', '`', '*', '?', '[', '{']
        common_shell_commands = ['echo', 'cat', 'grep', 'sed', 'awk', 'ls', 'cd', 'pwd', 'exit', 'test']
        
        # Check if it looks like a shell command
        has_shell_operators = any(char in first_arg for char in shell_indicators)
        has_quotes_with_spaces = ("'" in first_arg or '"' in first_arg) and ' ' in first_arg
        starts_with_shell_command = any(first_arg.startswith(cmd + ' ') or first_arg == cmd 
                                      for cmd in common_shell_commands)
        has_spaces_and_path = ' ' in first_arg and ('/' in first_arg or first_arg.startswith('.'))
        
        is_shell_command = has_shell_operators or has_quotes_with_spaces or starts_with_shell_command or has_spaces_and_path
        
        if is_shell_command:
            # Shell command - use first arg as full command
            command = first_arg
            use_shell = True
        else:
            # Script command - build from path and args
            if self._path is None:
                # No path provided, treat first arg as script name
                script_name = first_arg
                remaining_args = args[1:] if len(args) > 1 else []
            else:
                # Use provided path
                script_name = str(self._path)
                remaining_args = args
            
            cmd_args = [str(arg) for arg in remaining_args]
            for key, value in kwargs.items():
                flag = f"--{key.replace('_', '-')}"
                if isinstance(value, bool):
                    if value:
                        cmd_args.append(flag)
                else:
                    cmd_args.extend([flag, str(value)])
            command = [script_name] + cmd_args
            use_shell = False
        
        # Prepare stdin input (unified for both modes)
        input_data = None
        if stdin_input is not None:
            if isinstance(stdin_input, dict):
                input_data = _json.dumps(stdin_input).encode('utf-8')
            elif isinstance(stdin_input, list):
                input_data = _json.dumps(stdin_input).encode('utf-8')
            elif isinstance(stdin_input, str):
                input_data = stdin_input.encode('utf-8')
            elif isinstance(stdin_input, (bytes, bytearray)):
                input_data = bytes(stdin_input)
            elif isinstance(stdin_input, Iterable):
                input_data = '\n'.join(str(line) for line in stdin_input).encode('utf-8')
        
        # Execute with unified subprocess.run
        # Use repo environment if executing a script path
        env = None
        try:
            from ..repo import get_repo_env_for_script
            script_hint = None
            if not use_shell:
                if isinstance(command, list) and command:
                    script_hint = Path(command[0]) if "/" in str(command[0]) else None
            if script_hint and script_hint.exists():
                env = get_repo_env_for_script(script_hint)
        except Exception:
            env = None

        proc = subprocess.run(
            command,
            input=input_data,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=use_shell,
            text=False,
            env=env
        )
        return CompletedScriptResult(stdout=proc.stdout, stderr=proc.stderr)


class ShellScript(Executable):
    def __init__(self, executable: Path | str):
        executable = Path(executable)
        if not executable.exists():
            path = shutil.which(str(executable))
            if path is None:
                raise RuntimeError(f"Cannot find executable for {executable} in the system path")
            executable = Path(path)
        super().__init__(executable)

    def __call__(self, *args, stdin_input=None, **kwargs) -> CompletedScriptResult:
        return super().__call__(*args, stdin_input=stdin_input, **kwargs)

