import json as _json
import sys
from typing import Generator


def read_stdin_as_json() -> dict:
    return _json.load(sys.stdin)


def read_stdin_as_jsonl() -> Generator[dict, None, None]:
    for line in sys.stdin:
        yield _json.loads(line.strip())