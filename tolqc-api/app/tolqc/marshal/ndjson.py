import json
from collections.abc import Iterable
from typing import Any


def ndjson_rows_from_stream(stream: Iterable):
    for line in stream:
        yield parse_ndjson_row(line)


def parse_ndjson_row(line: str) -> dict:
    if len(line) > 100_000:
        # Don't get hung up parsing excessively large strings
        msg = f'Unexpectedly long line ({len(line):_d} characters) in input'
        raise ValueError(msg)
    row = json.loads(line)
    if type(row) is not dict:
        msg = f'JSON must decode to a dict, not a {type(row)}'
        raise ValueError(msg)
    return cleanup(row)


def cleanup(x: Any) -> Any:
    """Cleanup any strings within dicts and lists. Returns new objects"""
    if type(x) is str:
        return cleanup_string_whitespace(x)
    elif type(x) is list:
        return [cleanup(a) for a in x]
    elif type(x) is dict:
        new = {}
        for k, v in x.items():
            if type(k) is not str:
                msg = f'Keys must be strings not {type(k)}'
                raise ValueError(msg)
            new_k = cleanup_string_whitespace(k)
            if new_k is None:
                msg = f'Keys cannot be whitespace: {k!r}'
                raise ValueError(msg)
            new[new_k] = cleanup(v)
        return new
    else:
        return x


def cleanup_string_whitespace(s: str) -> str | None:
    """Strip whitespace and return `None` if string was entirely whitespace"""
    stripped = s.strip()
    return None if stripped == '' else stripped


def must_get_row_value(row: dict, key: str) -> Any:
    if val := row.get(key):
        return val
    msg = row_message(row, f"Missing '{key}' field in row")
    raise ValueError(msg)


def row_message(row: dict, msg: str) -> str:
    return f'{msg}:\n{format_row(row)}'


def format_row(row: dict) -> str:
    name_max = max(len(name) for name in row)
    return ''.join(f'  {name:>{name_max}} = {row[name]!r}\n' for name in row)
