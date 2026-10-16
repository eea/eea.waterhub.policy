PYTHON ?= python3.12
VENV ?= .venv

.PHONY: help install test lint format clean

help:
	@echo "eea.waterhub.policy commands:"
	@echo "  make install  Create the virtual environment and install test dependencies"
	@echo "  make test     Run the test suite"
	@echo "  make lint     Check Python formatting and lint rules"
	@echo "  make format   Format Python sources and fix lint violations"
	@echo "  make clean    Remove generated development files"

install:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install --editable ".[test]"

test:
	$(VENV)/bin/pytest

lint:
	$(VENV)/bin/ruff check src tests
	$(VENV)/bin/ruff format --check src tests

format:
	$(VENV)/bin/ruff check --fix src tests
	$(VENV)/bin/ruff format src tests

clean:
	rm -rf .coverage .pytest_cache .ruff_cache .venv build dist htmlcov
	find src tests -type d -name __pycache__ -prune -exec rm -rf {} +
	find src -type d -name '*.egg-info' -prune -exec rm -rf {} +

