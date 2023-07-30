FROM python:3.11-slim

COPY ./weebAPI /app/src
COPY ./requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt 

EXPOSE 8000

CMD ["uvicorn", "weebAPI.endpoints:app","--host=0.0.0.0","--reload"]


