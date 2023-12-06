# syntax=docker/dockerfile:1

FROM python:3.9-alpine

WORKDIR /ot-2

COPY ./src ./

RUN pip install --no-cache-dir -r requirements.txt