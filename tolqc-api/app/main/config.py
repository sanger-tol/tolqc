# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import os
import logging

def _get_environment():
    deployment_environment = os.getenv("ENVIRONMENT", "")
    if deployment_environment != "":
        return deployment_environment

    # if unset, assume dev
    logging.warning("$ENVIRONMENT is unset - assuming a 'dev' environment")
    return "dev"

deployment_environment = _get_environment()
