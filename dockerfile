FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requerimentos.txt

EXPOSE 8000

CMD ["uvicorn", "principal:app", "--host", "0.0.0.0", "--port", "8000"]
