# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.config import deployment_environment
from flask_restx import fields, Resource, Namespace


environment_namespace = Namespace(
    'environments',
    description='Deployment environment related methods',
)


environment_model = environment_namespace.model('Environment', {
    'environment': fields.String("dev"),
})


class EnvironmentResource(Resource):
    def __init__(self, api=None):
        super().__init__(api)

    @environment_namespace.doc('Gets the deployment environment string')
    @environment_namespace.response(
        200,
        description='Success',
        model=environment_model,
    )
    def get(self):
        return {'environment': deployment_environment}, 200


environment_namespace.add_resource(EnvironmentResource, '')
