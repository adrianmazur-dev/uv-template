from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

from ...config import settings
from ...logging import setup_logging

if TYPE_CHECKING:
    from arq.worker import Worker

logger = logging.getLogger(__name__)


async def startup_handler(ctx: dict[str, Any]) -> None:
    setup_logging(settings.environment, settings.log_level)
    logger.info("Worker starting up")
