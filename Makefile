_install-venv:
	pip install poetry==1.7.1
	poetry env use 3.12
	poetry install

linter-check:
	poetry run flake8 backend
