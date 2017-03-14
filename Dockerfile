FROM python:3.6-alpine

USER root

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

EXPOSE 8337

CMD ./manage.py runserver 0.0.0.0:8337
