FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1

ADD . /test_django_doc
WORKDIR /test_django_doc

RUN apt-get update
RUN apt-get install -y python-gdal
RUN pip install --upgrade pip

COPY requirements.txt /test_django_doc/
RUN pip install -r requirements.txt
COPY . /test_django_doc/