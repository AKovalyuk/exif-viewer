FROM python:3.11.0-slim-buster

ARG APP_HOME

RUN apt-get update && \
    apt-get install --no-install-recommends -y libpq-dev build-essential

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY . ${APP_HOME}
WORKDIR ${APP_HOME}

RUN pip install -r ${APP_HOME}/requirements.txt