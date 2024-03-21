PROJECT_NAME ?= telegram2logseq

all:
	@echo "make format\t— Format code with black & isort"


format:
	poetry run python3 -m black $(PROJECT_NAME)
	poetry run python3 -m isort $(PROJECT_NAME)
