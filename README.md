<!--
SPDX-FileCopyrightText: 2021 Genome Research Ltd.

SPDX-License-Identifier: MIT
-->

## Running with K8S

To run locally, or even remotely manually, follow the instruction below. You will need a file set up with the necessary environment variables. Let's call this values-dev.yaml:
```bash
helm install --values values-dev.yaml tolqc-app

```

## Running with Docker

To run the app on a Docker container, first you will need to set up a file with the necessary environment variables. Let's call this .env.dev (there is a template file .env.template you can use as a template!). Then, execute the following from the root directory:

```bash
# running the app (devlopment) - N.B. database will need initialising
docker-compose --env-file .env.dev up --build --abort-on-container-exit tolqc-api tolqc-ui tolqc-db

# Running API tests
docker-compose --env-file .env.dev up --build --abort-on-container-exit tolqc-api-test

# Running UI tests (watch mode)
docker-compose --env-file .env.dev up --build --abort-on-container-exit tolqc-ui-test

```
Everything for staging and prod is built/tested/deployed via GitLab. Commit to the staging or production branch to trigger the pipeline.
