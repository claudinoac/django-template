FROM python:3.7-alpine

RUN apk add gcc \
            libzmq \
            musl-dev \
            zeromq-dev \
            mariadb-client \
            mariadb-connector-c-dev \
            sqlite 

RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
RUN apk --update add postgresql-dev gcc musl-dev

RUN pip3.7 install -U pip setuptools

RUN mkdir /code
COPY django_template /code/
WORKDIR /code/requirements
RUN pip install -r ./development.txt
WORKDIR /code
EXPOSE 3000
