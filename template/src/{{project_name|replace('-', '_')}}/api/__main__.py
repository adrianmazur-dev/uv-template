from __future__ import annotations

import uvicorn

from ..config import settings

def main():
    uvicorn.run(
        "{{ project_name | replace('-', '_') }}.api:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.api_reload,
    )

if __name__ == "__main__":
    main()
