from __future__ import annotations

from arq.worker import run_worker

from .settings import WorkerSettings

if __name__ == "__main__":
    run_worker(WorkerSettings)  # type: ignore[arg-type]
