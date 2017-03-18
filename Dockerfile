FROM python:3.6-alpine

USER root

COPY requirements.txt /tmp/

# inspired by https://github.com/blurrcat/alpine-python-psycopg2/blob/master/Dockerfile
RUN apk add --no-cache --virtual build-deps gcc python3-dev musl-dev \
  && apk add --no-cache postgresql-dev \
  && pip install --no-cache-dir -r /tmp/requirements.txt \
  && apk del build-deps

EXPOSE 8337

CMD ./manage.py runserver 0.0.0.0:8337
