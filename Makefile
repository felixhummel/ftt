shell:
	docker-compose run app ./manage.py shell
migrate:
	docker-compose run app ./manage.py migrate
makemigrations:
	docker-compose run app ./manage.py makemigrations
fixtures:
	docker-compose run app ./manage.py loaddata admin
	docker-compose run app ./manage.py loaddata groups
	docker-compose run app ./manage.py loaddata projects

recreate_db:
	docker-compose up -d postgres 
	docker-compose exec --user postgres postgres dropdb ftt
	docker-compose exec --user postgres postgres createdb ftt
	make migrate
	make fixtures
