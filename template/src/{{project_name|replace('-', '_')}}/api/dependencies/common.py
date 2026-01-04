from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...config import Settings


def get_settings() -> Settings:
    from ...config import settings

    return settings
