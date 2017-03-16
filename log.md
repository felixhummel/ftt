```
docker-compose run app django-admin startproject proj_ftt .
docker-compose run app ./manage.py startapp ftt
docker-compose run app ./manage.py migrate
```

- How to Login: https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html
- Ref: https://docs.djangoproject.com/en/1.10/topics/auth/default/
```
docker-compose run app ./manage.py createsuperuser --username admin --noinput --email admin@example.org
docker-compose run app ./manage.py set_password admin admin
# admin fixture
docker-compose run app ./manage.py dumpdata auth.User > ftt/fixtures/admin.json
docker-compose run app ./manage.py loaddata admin
```

http://stackoverflow.com/questions/34818114/using-date-picker-from-django-admin
