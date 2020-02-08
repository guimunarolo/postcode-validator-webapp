test:
	pipenv run pytest -sx webapp/tests/

pyformat:
	black webapp/.

deploy:
	git push heroku master
