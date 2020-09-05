FROM ubuntu:focal

WORKDIR /code

RUN apt-get update && \
  apt-get install --no-install-recommends --yes \
  python3 \
  python3-pip

ENV FLASK_APP ./backend/applications/server.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_ENV development
ENV AWS_ACCESS_KEY_ID $AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY $AWS_SECRET_ACCESS_KEY
ENV FLASK_SECRET_KEY $FLASK_SECRET_KEY
