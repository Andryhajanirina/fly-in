PYTHON = .venv/bin/python
VENV = .venv

.PHONY: install run debug clean lint lint-strict

install:
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install pytest flake8 mypy

run:
	PYTHONPATH=src $(PYTHON) -m fly_in

debug:
	PYTHONPATH=src $(PYTHON) -m pdb -m fly_in

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache .mypy_cache

lint:
	$(PYTHON) -m flake8 .
	$(PYTHON) -m mypy . \
		--warn-return-any \
		--warn-unused-ignores \
		--ignore-missing-imports \
		--disallow-untyped-defs \
		--check-untyped-defs

lint-strict:
	$(PYTHON) -m flake8 .
	$(PYTHON) -m mypy . --strict

test:
	$(PYTHON) -m pytest