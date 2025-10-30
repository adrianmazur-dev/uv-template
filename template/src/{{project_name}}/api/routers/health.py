from __future__ import annotations

from fastapi import APIRouter

from ...config import settings
from ..schemas.responses.base import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    return HealthResponse(
        status="ok",
        version="0.1.0",
        environment=settings.environment.value,
    )
