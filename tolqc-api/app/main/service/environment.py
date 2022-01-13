# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask import current_app as app


class EnvironmentService:
    @classmethod
    def get_environment(self):
        return {'environment': app.config['DEPLOYMENT_ENVIRONMENT']}
