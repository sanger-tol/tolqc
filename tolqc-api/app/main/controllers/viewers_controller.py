# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask import jsonify
import os
import logging


def get_environment():
    deployment_environment = os.getenv("ENVIRONMENT")
    if deployment_environment is not None and deployment_environment != "":
        return jsonify({'environment': deployment_environment})

    # if unset, assume dev
    logging.warn("$ENVIRONMENT is unset - assuming a 'dev' environment")
    return jsonify({'environment': 'dev'})
