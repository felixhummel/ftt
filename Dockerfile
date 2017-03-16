FROM python:3.6-alpine

USER root

# https://github.com/blurrcat/alpine-python-psycopg2/blob/master/Dockerfile
RUN apk add --no-cache --virtual build-deps gcc python3-dev musl-dev \
  && apk add --no-cache postgresql-dev \
  && pip install psycopg2 \
  && apk del build-deps

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

EXPOSE 8337

CMD ./manage.py runserver 0.0.0.0:8337
