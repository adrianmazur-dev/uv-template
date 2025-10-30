from __future__ import annotations

from ..base import BaseSchema


class ErrorResponse(BaseSchema):
    detail: str
    error_code: str | None = None
