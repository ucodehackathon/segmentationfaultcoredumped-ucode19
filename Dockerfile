FROM python:3.6-alpine
RUN apk update
RUN apk add gcc python3-dev musl-dev \
    && apk add postgresql-dev postgresql-client
RUN apk add linux-headers
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/