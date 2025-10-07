# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

FROM gitlab-registry.internal.sanger.ac.uk/tol/tol-core/api-base:1.0.5

ENV PYTHONDONTWRITEBYTECODE=1
ENV UWSGI_CHEAPER=4
ENV UWSGI_PROCESSES=64
ENV VIRTUAL_ENV=/app

WORKDIR "$VIRTUAL_ENV"
RUN python3 -m venv "$VIRTUAL_ENV"
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip3 --no-cache-dir install --upgrade pip

COPY ./app app
COPY ./pyproject.toml .
COPY ./README.md .
COPY ./migrations /migrations
RUN pip3 --no-cache-dir install . 'tolqc-api'
