from __future__ import annotations

from arq.worker import run_worker

from .settings import WorkerSettings

def main():
    run_worker(WorkerSettings)  # pyright: ignore[reportArgumentType]

if __name__ == "__main__":
    main()
