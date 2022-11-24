# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
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

COPY nginx.conf /etc/nginx/

## Remove default nginx index page
RUN rm -rf /var/www/tolqc-ui/*

# Copy from the stage 1
COPY --from=builder /workspace/build/ /var/www/tolqc-ui/

EXPOSE 80
