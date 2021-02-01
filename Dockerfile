FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /products

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
