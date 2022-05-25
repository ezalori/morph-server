default: web

web:
	./ve flask run

dev:
	./ve pip install -r requirements.txt -r requirements-dev.txt

test:
	./ve pylint -rn vault tests
	./ve mypy vault tests
	./ve pytest tests
