from ._script_metadata import ScriptMetadata
from ..shell.script_wrapper import ShellScript, CompletedScriptResult


def runscript(script: ScriptMetadata, *args, **kwargs) -> CompletedScriptResult:
    return ShellScript(script.script_path)(*args, **kwargs)

