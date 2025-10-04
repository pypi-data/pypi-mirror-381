from dataclasses import dataclass
from pathlib import Path
from typing import Literal

OutputType = Literal["json", "text"]


@dataclass
class ScriptMetadata:
    script_path: Path
    output_type: OutputType
