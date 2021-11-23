# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask import current_app as app
from flask_restx import fields, Resource, Namespace


environment_namespace = Namespace(
    'environment',
    description='Deployment environment related methods',
)


environment = environment_namespace.model('Environment', {
    'environment': fields.String("The environment string of the server"),
})


class EnvironmentResource(Resource):
    def __init__(self, api=None):
        super().__init__(api)
        self._environment = app.config["DEPLOYMENT_ENVIRONMENT"]

    @environment_namespace.doc('Gets the deployment environment string')
    def get(self):
        return {'environment': self._environment}, 200
