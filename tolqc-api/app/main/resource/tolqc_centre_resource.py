# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import TolqcCentreSchema
from flask_restx import Namespace, Resource


centre_namespace = Namespace('centre', description='Centre related methods')

get_centre_model = centre_namespace.model(
    'GET Centre Model',
    TolqcCentreSchema.to_api_model_dict()
)

post_centre_model = centre_namespace.model(
    'POST Centre Model',
    TolqcCentreSchema.to_api_model_dict_exclude_id()
)


class TolqcCentreDetailResource(Resource):
    name = 'centre'


class TolqcCentreListResource(Resource):
    name = 'centres'

    @centre_namespace.expect(post_centre_model)
    @centre_namespace.response(
        200,
        description='Success',
        model=get_centre_model,
    )
    @centre_namespace.response(
        400,
        description='Error'
    )
    def post(self, data):
        pass


centre_namespace.add_resource(TolqcCentreDetailResource, '/<int:id>')
centre_namespace.add_resource(TolqcCentreListResource, '')
