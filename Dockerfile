FROM python:3.12.3-slim-bookworm

RUN apt-get update && apt-get install -y make && apt-get clean

ENV PYTHONUNBUFFERED=1
WORKDIR /

COPY ./main.py /main.py
COPY ./Makefile /Makefile
COPY *.sh /

# To avoid defining multiple Dockerfiles we do not define the CMD here
