FROM python:3.12-slim-bullseye AS python-base

COPY requirements.txt ./

RUN pip install -r requirements.txt

ENV PYTHONNONBUFFERED=1
ENV PYTHONPATH=.

RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . .

COPY .env .

EXPOSE 8000

ENTRYPOINT [ "daphne", "-p", "8000", "-b", "0.0.0.0", "app.asgi:application" ]