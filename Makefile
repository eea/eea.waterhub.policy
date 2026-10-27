PYTHON ?= python3.12
VENV ?= .venv

.PHONY: help install test test-ci coverage lint format package ci clean

help:
	@echo "eea.waterhub.policy commands:"
	@echo "  make install  Create the virtual environment and install test dependencies"
	@echo "  make test     Run the test suite"
	@echo "  make test-ci  Run tests and create JUnit and coverage reports"
	@echo "  make coverage Show the generated HTML coverage report location"
	@echo "  make lint     Check Python formatting and lint rules"
	@echo "  make format   Format Python sources and fix lint violations"
	@echo "  make package  Build and validate source and wheel distributions"
	@echo "  make ci       Run the strict lint, test, and package checks"
	@echo "  make clean    Remove generated development files"

install:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install --editable ".[test]"

test:
	$(VENV)/bin/pytest

test-ci:
	mkdir -p xunit-reports-current/coverage
	$(VENV)/bin/pytest \
		--junitxml=xunit-reports-current/junit.xml \
		--cov=eea.waterhub.policy \
		--cov-report=term-missing \
		--cov-report=xml:xunit-reports-current/coverage/coverage.xml \
		--cov-report=lcov:xunit-reports-current/coverage/lcov.info \
		--cov-report=html:xunit-reports-current/coverage/lcov-report

coverage:
	@echo "Coverage report: xunit-reports-current/coverage/lcov-report/index.html"

lint:
	$(VENV)/bin/ruff check src
	$(VENV)/bin/ruff format --check src

format:
	$(VENV)/bin/ruff check --fix src
	$(VENV)/bin/ruff format src

package:
	rm -rf build dist
	$(VENV)/bin/python -m build
	$(VENV)/bin/twine check dist/*

ci: lint test-ci package

clean:
	rm -rf .coverage .pytest_cache .ruff_cache .venv build dist htmlcov xunit-reports-current
	find src -type d -name __pycache__ -prune -exec rm -rf {} +
	find src -type d -name '*.egg-info' -prune -exec rm -rf {} +

