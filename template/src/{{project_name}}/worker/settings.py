from __future__ import annotations

from arq.connections import RedisSettings

from ..config import settings
from .handlers.shutdown import shutdown_handler
from .handlers.startup import startup_handler
from .tasks import get_task_functions


class WorkerSettings:
    redis_settings: RedisSettings = RedisSettings.from_dsn(settings.redis_url)
    functions = get_task_functions()
    on_startup = startup_handler
    on_shutdown = shutdown_handler
    max_jobs: int = settings.worker_max_jobs
    max_tries: int = settings.worker_max_tries
    job_timeout: int = settings.worker_timeout
