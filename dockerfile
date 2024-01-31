# syntax=docker/dockerfile:1

FROM python:3.9-alpine

WORKDIR /ot-2

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src ./

ENTRYPOINT ["python3", "-m", "opentrons.simulate", "./cell_free_round/round6/20240202.py"]