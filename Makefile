run-unit-tests:
	docker-compose run server coverage run manage.py test
run-integration-tests:
	docker-compose run server sh -c 'coverage run /usr/local/bin/behave apps/**/tests/integration'
