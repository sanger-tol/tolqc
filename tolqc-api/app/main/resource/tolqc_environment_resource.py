# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask import current_app as app
from flask_restx import fields, Resource, Namespace


environment_namespace = Namespace(
    'environments',
    description='Deployment environment related methods',
)


environment_model = environment_namespace.model('Environment', {
    'environment': fields.String("dev", required=True),
})


class EnvironmentResource(Resource):
    def __init__(self, api=None):
        super().__init__(api)
        self._environment = app.config['DEPLOYMENT_ENVIRONMENT']

    @environment_namespace.doc('Gets the deployment environment string')
    @environment_namespace.response(
        200,
        description='Success',
        model=environment_model,
    )
    def get(self):
        return {'environment': self._environment}, 200


environment_namespace.add_resource(EnvironmentResource, '')
