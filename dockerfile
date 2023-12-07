# syntax=docker/dockerfile:1

FROM python:3.9-alpine

WORKDIR /ot-2

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src ./

