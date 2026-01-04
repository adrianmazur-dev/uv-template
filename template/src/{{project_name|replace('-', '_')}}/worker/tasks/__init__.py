from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable


def get_task_functions() -> list[Callable[..., object]]:
    return []
