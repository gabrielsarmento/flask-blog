FROM python:3.6
ENV PYTHONUNBUFFERED 1
WORKDIR /flaskblog

ADD ./ ./

RUN pip install -r requirements.txt
ADD . ./
