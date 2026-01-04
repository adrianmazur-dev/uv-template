# uv-template

A modern Python project template using [uv](https://github.com/astral-sh/uv) and [Copier](https://github.com/copier-org/copier).

## Features

- **Fast & Modern**: Built on `uv` for lightning-fast dependency management.
- **Microservices Ready**: Optional FastAPI and ARQ (worker) integration.
- **Quality Tooling**: Pre-configured Ruff, Basedpyright, and Codespell.
- **Workflow Automation**: Ready-to-use scripts for linting, testing, and cleaning.

## Creating a Project

To create a new project based on this template, ensure you have `uv` and `copier` installed, then run:

```bash
uv tool run copier copy gh:adrianmazur-dev/uv-template path/to/your-project
```

Or if you have the template locally:

```bash
uv tool run copier copy /path/to/uv-template path/to/your-project
```

## Updating a Project

To pull the latest changes from the template into your existing project:

```bash
cd your-project
uv tool run copier update
```

## Scripts Usage

Inside your generated project, you can use the following commands:

- `uv run lint`: Run Ruff and Codespell.
- `uv run test`: Run Pytest.
- `uv run start-api`: Start FastAPI server (if included).
- `uv run start-worker`: Start ARQ worker (if included).
- `uv run clean`: Remove build artifacts and cache.
- `uv run upgrade`: Upgrade all dependencies to their latest versions.

## Development

To work on the template itself:

1. Clone the repository.
2. Install dependencies: `uv sync`.
3. Test the template locally: `uv tool run copier copy . ../test-project`.
