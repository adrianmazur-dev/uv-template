.DEFAULT_GOAL := default

.PHONY: default install lint test upgrade build clean

default: install lint test clean

install:
	uv sync --all-extras

lint:
	uv run codespell --write-changes src tests README.md
	uv run ruff check --fix src tests
	uv run ruff format src tests
	uv run basedpyright --stats src tests

test:
	uv run pytest

upgrade:
	uv sync --upgrade --all-extras --dev

build:
	uv build

clean:
	-rm -rf dist/
	-rm -rf *.egg-info/
	-rm -rf .pytest_cache/
	-rm -rf .mypy_cache/
	-rm -rf .venv/
	-find . -type d -name "__pycache__" -exec rm -rf {} +