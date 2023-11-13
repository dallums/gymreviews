FROM python:3-alpine3.15
WORKDIR /app
COPY . /app
RUN python -m venv /env/