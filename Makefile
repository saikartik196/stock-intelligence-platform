install:
	pip install -e .

format:
	black src tests

lint:
	ruff src tests

test:
	pytest
