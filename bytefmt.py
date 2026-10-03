"""Format byte counts and parse them back."""
from __future__ import annotations

_UNITS = ("B", "KB", "MB", "GB", "TB")


def format_bytes(size: int) -> str:
    if size < 0:
        raise ValueError("字节数不能为负")
    value = float(size)
    index = 0
    while value >= 1024 and index < len(_UNITS) - 1:
        value /= 1024
        index += 1
    if index == 0:
        return f"{int(value)} B"
    text = f"{value:.1f}".rstrip("0").rstrip(".")
    return f"{text} {_UNITS[index]}"


def parse_bytes(text: str) -> int:
    raw = (text or "").strip().replace(" ", "")
    if not raw:
        raise ValueError("空字符串")
    unit = "B"
    number = raw
    for name in sorted(_UNITS, key=len, reverse=True):
        if raw.upper().endswith(name):
            unit = name
            number = raw[: -len(name)]
            break
    try:
        amount = float(number)
    except ValueError as exc:
        raise ValueError(f"无法解析: {text}") from exc
    if amount < 0:
        raise ValueError("字节数不能为负")
    power = _UNITS.index(unit)
    return int(amount * (1024**power))


def greater_than(left: str, right: str) -> bool:
    return parse_bytes(left) > parse_bytes(right)


def sum_bytes(*texts: str) -> int:
    if not texts:
        raise ValueError("没有字节数")
    return sum(parse_bytes(text) for text in texts)


def is_bytes(text: str) -> bool:
    try:
        parse_bytes(text)
    except ValueError:
        return False
    return True
