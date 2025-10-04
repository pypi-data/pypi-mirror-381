import json
from typing import Any, Dict, Union
from click import secho
from ..shell.script_wrapper import CompletedScriptResult


def printjson(obj: Union[Dict[str, Any], CompletedScriptResult]) -> None:
    if isinstance(obj, CompletedScriptResult):
        printjson(obj.json())
    else:
        print(json.dumps(obj, indent=2))


def printformatted(obj: Any) -> None:
    if isinstance(obj, dict):
        printjson(obj)
    elif isinstance(obj, bytes):
        print(obj.decode())
    else:
        print(obj)


class _Print:
    def green(self, obj: Any) -> None:
        secho(obj, fg="green")

    def confirm(self, obj: Any) -> None:
        self.green(obj)

    def red(self, obj: Any) -> None:
        secho(obj, fg="red")

    def error(self, obj: Any) -> None:
        self.red(obj)

    def blue(self, obj: Any) -> None:
        secho(obj, fg="blue")

    def info(self, obj: Any) -> None:
        self.blue(obj)

    def yellow(self, obj: Any) -> None:
        secho(obj, fg="yellow")

    def warn(self, obj: Any) -> None:
        self.yellow(obj)

    def warn_stderr(self, obj: Any) -> None:
        secho(obj, fg="yellow", err=True)

    def error_stderr(self, obj: Any) -> None:
        secho(obj, fg="red", err=True)

    def plain(self, obj: Any) -> None:
        print(obj)

    def json(self, obj: Any) -> None:
        printjson(obj)


Print = _Print()
