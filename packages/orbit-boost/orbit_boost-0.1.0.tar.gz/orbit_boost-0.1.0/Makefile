.PHONY: help setup lint test build clean

help:
	@echo "Targets:"
	@echo "  setup   - install dev deps"
	@echo "  lint    - run ruff and mypy"
	@echo "  test    - run pytest"
	@echo "  build   - build wheel and sdist"
	@echo "  clean   - remove build artifacts"

setup:
	pip install -e .[dev]
	pre-commit install

lint:
	ruff check .
	mypy src || true

test:
	pytest

build:
	python -m pip install -U build
	python -m build

clean:
	rm -rf build dist *.egg-info
	find . -name "__pycache__" -type d -exec rm -rf {} +
