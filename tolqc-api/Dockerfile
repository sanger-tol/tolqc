# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

FROM gitlab-registry.internal.sanger.ac.uk/tol/tol-core/api-base:1.0.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV UWSGI_CHEAPER 4
ENV UWSGI_PROCESSES 64

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-setuptools

COPY app/requirements.txt /app
COPY app/setup.py /app

RUN pip3 install --upgrade setuptools
RUN python3 setup.py install

RUN pip3 --no-cache-dir install -r requirements.txt

COPY ./app /app
COPY ./migrations /migrations
