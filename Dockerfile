FROM python:3-alpine

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

WORKDIR /app
CMD python script.py
