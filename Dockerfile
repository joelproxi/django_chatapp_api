FROM python:3.12-slim-bullseye 

RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    build-essential && pip install --no-cache-dir --upgrade pip 

WORKDIR /chatapp
COPY ./requirements.txt /chatapp/

RUN pip install --no-cache-dir --requirement /chatapp/requirements.txt 

COPY . /chatapp

EXPOSE 8000

