FROM python:3-alpine
LABEL name="DRF Template" \
      version='1.0.0'

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
WORKDIR /code
COPY requirements.txt /code/
RUN python3 -m venv venv
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/
