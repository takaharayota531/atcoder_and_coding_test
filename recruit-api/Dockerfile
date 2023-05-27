FROM python:3.8

USER root

RUN apt-get update && apt-get upgrade -y

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

ENV PYTHONPATH .

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]