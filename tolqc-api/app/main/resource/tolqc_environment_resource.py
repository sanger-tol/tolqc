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
    'environment': fields.String("dev"),
})


class EnvironmentResource(Resource):
    environment = app.config["DEPLOYMENT_ENVIRONMENT"]

    @environment_namespace.doc('Gets the deployment environment string')
    @environment_namespace.response(
        200,
        description='Success',
        model=environment_model,
    )
    def get(self):
        return {'environment': self.environment}, 200


environment_namespace.add_resource(EnvironmentResource, '')
