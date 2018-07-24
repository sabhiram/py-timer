test:
	@python -m unittest discover -s . -p '*_test.py'

lint:
	@flake8 --ignore=E221,E241,E721 pytimer/

.PHONY: lint test
