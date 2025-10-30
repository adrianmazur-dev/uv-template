from __future__ import annotations

from typing import Any


def is_valid_email(email: str) -> bool:
    return "@" in email and "." in email.split("@")[-1]


def is_not_empty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    return bool(value)
