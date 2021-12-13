# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask import current_app as app
from flask_restx import Resource

from main.swagger.environment import EnvironmentSwagger


api_environment = EnvironmentSwagger.api


@api_environment.route('')
class EnvironmentResource(Resource):
    def __init__(self, api=None):
        super().__init__(api)
        self._environment = app.config['DEPLOYMENT_ENVIRONMENT']

    @api_environment.doc('Gets the deployment environment string')
    @api_environment.response(
        200,
        description='Success',
        model=EnvironmentSwagger.response_model,
    )
    def get(self):
        return {'environment': self._environment}, 200
