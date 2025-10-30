DEFAULT_GOAL := default

.PHONY: lint test clean

default: install lint clean test

install:
	uv sync --all-extras

lint:
	uv run python -m devtools.lint

test:
	@echo "Testing uv-template..."
	@TEST_DIR=$$(mktemp -d); \
	trap "rm -rf $$TEST_DIR" EXIT; \
	echo "Generating test project in $$TEST_DIR"; \
	if copier copy --defaults \
		--data project_name="test-project" \
		--data project_description="Test project" \
		--data project_author_name="Test Author" \
		--data project_author_email="test@example.com" \
		--data include_fastapi=true \
		--data include_arq=true \
		. "$$TEST_DIR/test-project" \
		--trust; then \
		echo "✓ Template generation succeeded!"; \
	else \
		echo "✗ Template generation failed!"; \
		exit 1; \
	fi

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
