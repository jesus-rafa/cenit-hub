FROM python:3.9

RUN pip install --upgrade pip

RUN apt-get update

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./cenit_hub /app

WORKDIR /app

CMD ["python", "cenit_hub.py"]