# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask import current_app as app


class EnvironmentService:
    @classmethod
    def get_environment(cls):
        return {'environment': app.config['DEPLOYMENT_ENVIRONMENT']}
