FROM python:3.8

WORKDIR /opt/benj

ENV PYTHONPATH "${PYTHONPATH}:/opt/benj"


RUN pip install pygame

COPY . .
