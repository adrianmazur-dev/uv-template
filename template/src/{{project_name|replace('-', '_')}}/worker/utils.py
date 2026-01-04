from __future__ import annotations

from typing import TYPE_CHECKING, Any

from arq import create_pool
from arq.connections import RedisSettings

from ..config import settings

if TYPE_CHECKING:
    from arq.connections import ArqRedis


async def get_redis_pool() -> ArqRedis:
    redis_settings = RedisSettings.from_dsn(settings.redis_url)
    return await create_pool(redis_settings)


async def enqueue_job(job_name: str, *args: Any, **kwargs: Any) -> str | None:
    redis = await get_redis_pool()
    try:
        job = await redis.enqueue_job(job_name, *args, **kwargs)
        return job.job_id if job else None
    finally:
        await redis.close()
