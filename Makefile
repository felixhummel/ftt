migrate:
	docker-compose run app ./manage.py migrate
admin:
	docker-compose run app ./manage.py loaddata admin

