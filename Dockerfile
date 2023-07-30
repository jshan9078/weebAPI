FROM python:3.11-slim

COPY ./weebAPI /app/src
COPY ./requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt 


