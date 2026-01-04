from __future__ import annotations

from collections.abc import Callable
from typing import Any

from arq.connections import RedisSettings

from ..config import settings
from .handlers.shutdown import shutdown_handler
from .handlers.startup import startup_handler
from .tasks import get_task_functions


class WorkerSettings:
    redis_settings: RedisSettings = RedisSettings.from_dsn(settings.redis_url)
    functions: list[Callable[..., Any]] | None = get_task_functions()
    on_startup: Callable[..., Any] | None = startup_handler
    on_shutdown: Callable[..., Any] | None = shutdown_handler
    max_jobs: int = settings.worker_max_jobs
    max_tries: int = settings.worker_max_tries
    job_timeout: int = settings.worker_timeout
