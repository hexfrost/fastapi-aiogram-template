_install-venv:
	pip install poetry==1.7.1
	poetry config virtualenvs.create false
	poetry install

linter-check:
	poetry run flake8 backend
