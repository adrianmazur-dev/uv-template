from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from arq.worker import Worker

logger = logging.getLogger(__name__)


async def shutdown_handler(ctx: dict[str, Any]) -> None:
    logger.info("Worker shutting down")
