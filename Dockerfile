FROM python:3.10-alpine

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /book_store
COPY . /book_store

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /book_store

USER appuser