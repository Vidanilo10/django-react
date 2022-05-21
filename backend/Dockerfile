FROM python:3.10-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /backend
RUN: gunicorn core.wsgi --bind 0.0.0.0:8000
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .