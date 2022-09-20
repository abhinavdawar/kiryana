FROM python:3.10.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /kiryana
WORKDIR /kiryana
ADD requirements.txt /kiryana/
RUN pip install — upgrade pip && pip install -r requirements.txt
ADD . /kiryana/