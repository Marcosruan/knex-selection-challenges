FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install -r requerimentos.txt

EXPOSE 8000

CMD alembic upgrade head && uvicorn principal:app --host 0.0.0.0 --port 8000
