test:
	pipenv run pytest -sx webapp/tests/

pyformat:
	black webapp/.

deploy:
	git push heroku master

run:
	pipenv run webapp/manage.py runserver 0:8000
