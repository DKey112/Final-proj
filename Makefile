PYTHON = python3

format:
	$(PYTHON) -m isort .
	$(PYTHON) -m black .
	$(PYTHON) -m flake8 .
	
check:
	$(PYTHON) -m isort --check .
	$(PYTHON) -m black --check .
	$(PYTHON) -m flake8 --check .

install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt