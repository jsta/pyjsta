.PHONY: docs

install:
	pip install --upgrade -e .

docs:
	mkdocs serve
