from __future__ import annotations

from ..base import BaseSchema


class BaseResponse(BaseSchema):
    pass


class HealthResponse(BaseSchema):
    status: str
    version: str
    environment: str
