# This file is part of the research.fi API service
#
# Copyright 2019 Ministry of Education and Culture, Finland
#
# :author: CSC - IT Center for Science Ltd., Espoo Finland servicedesk@csc.fi
# :license: MIT

FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/webapps

RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/webapps/Pipfile
RUN pipenv install --skip-lock --system --dev

COPY ./webapps /usr/src/webapps