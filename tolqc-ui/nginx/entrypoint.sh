#!/bin/sh

# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

envsubst "\$TOLQC_API_LOCATION" < /etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf && cat /etc/nginx/nginx.conf && nginx -g 'daemon off;'
