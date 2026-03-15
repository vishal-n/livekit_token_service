.PHONY: install run dev clean help

# Default target
help:
	@echo "LiveKit Token Service"
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  install   Install dependencies"
	@echo "  run      Start the server (with reload)"
	@echo "  dev      Alias for run"
	@echo "  clean    Remove cache and build artifacts"
	@echo "  help     Show this help"

install:
	pip install -r requirements.txt
	pip install fastapi uvicorn python-dotenv

run:
	python run.py

dev: run

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
