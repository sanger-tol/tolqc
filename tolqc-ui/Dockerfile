# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

# This is used for a production build
# stage 1 as builder
FROM node:12-alpine as builder

RUN apk add yarn
RUN mkdir /workspace

WORKDIR /workspace

COPY app/ .
RUN yarn install
RUN yarn build

# Stage 2
FROM nginx:alpine

## Remove default nginx index page
RUN rm -rf /var/www/tolqc-ui/*

# Copy from the stage 1
COPY --from=builder /workspace/build/ /usr/share/nginx/html/

EXPOSE 80
