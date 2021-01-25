FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1

ADD . /testtrycore
WORKDIR /testtrycore

RUN apt-get update
RUN apt-get install -y python-gdal
RUN pip install --upgrade pip

COPY requirements.txt /testtrycore/
RUN pip install -r requirements.txt
COPY . /testtrycore/