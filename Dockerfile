# Build the react app.
FROM node:12.18.2 as builder

WORKDIR /code

COPY ./frontend /code

RUN npm install
RUN npm run build

FROM ubuntu:focal

ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG FLASK_SECRET_KEY

ENV FLASK_APP ./applications/server.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_ENV development
ENV AWS_ACCESS_KEY_ID $AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY $AWS_SECRET_ACCESS_KEY
ENV FLASK_SECRET_KEY $FLASK_SECRET_KEY

# Copy the frontend build from the node image.
COPY --from=builder /code/build /code/build

WORKDIR /code

RUN apt-get update && \
  apt-get install --no-install-recommends --yes \
  python3 \
  python3-pip

COPY . /code

RUN pip3 install .

CMD ["flask", "run"]
