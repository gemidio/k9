format:
	poetry run black .
	poetry run isort .

lint:
	poetry run prospector --with-tool pydocstyle
	poetry run mypy .
