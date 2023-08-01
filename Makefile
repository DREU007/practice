export PYTHONPATH=.
run:
	poetry run ipython solution.py

dbug:
	poetry run python -m ipdb solution.py

test:
	poetry run pytest -vvv

test-dbug:
	poetry run pytest -s

lint:
	poetry run flake8 solution.py tests strategies
