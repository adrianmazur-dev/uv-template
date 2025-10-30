from __future__ import annotations

from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .._version import __version__
from ..config import settings
from ..logging import setup_logging
from .exceptions import register_exception_handlers
from .middlewares.request_id import RequestIDMiddleware
from .middlewares.timing import TimingMiddleware
from .routers import register_routers


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
    setup_logging(settings.environment, settings.log_level)
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version=__version__,
        lifespan=lifespan,
    )

    if settings.cors_origins:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.cors_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    app.add_middleware(RequestIDMiddleware)
    app.add_middleware(TimingMiddleware)

    register_routers(app)
    register_exception_handlers(app)

    return app


app = create_app()
