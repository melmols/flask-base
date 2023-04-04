FROM python:3.8-slim-buster

MAINTAINER Melanie Molina melanie@tryhackme.com

WORKDIR /app



COPY ./app/requirements.txt requirements.txt

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python3", "./app/app.py"]
