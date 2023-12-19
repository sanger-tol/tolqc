# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

# This is used for a production build
# stage 1 as builder
FROM node:18.16.0-alpine as builder

RUN apk add yarn
RUN mkdir /workspace

WORKDIR /workspace

RUN echo \"@tol:registry\" \"https://gitlab.internal.sanger.ac.uk/api/v4/projects/3596/packages/npm/\" >> .yarnrc

COPY app/ .
RUN yarn install --ignore-engines
RUN yarn build


# Stage 2
FROM gitlab-registry.internal.sanger.ac.uk/tol/tol-core/web-base:1.0.2

# Copy from the stage 1
COPY --from=builder /workspace/build/ /var/www/

EXPOSE 80
