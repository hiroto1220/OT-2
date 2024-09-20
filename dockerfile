# syntax=docker/dockerfile:1

FROM python:3.10-alpine

WORKDIR /ot-2

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src ./

ENTRYPOINT ["python3", "-m", "opentrons.simulate", "./cell_free_round/top10/20240212.py"]