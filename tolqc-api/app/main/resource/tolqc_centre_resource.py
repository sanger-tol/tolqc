# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Resource

from .base import BaseNamespace
from main.schema import TolqcCentreRequestSchema, \
                        TolqcCentreResponseSchema

centre_namespace = BaseNamespace(
    'centre',
    description='Centre related methods',
)

centre_response_model = centre_namespace.schema_model(
    'Centre Response-Model',
    TolqcCentreResponseSchema.to_schema_model_dict()
)

centre_request_model = centre_namespace.model(
    'Centre Request-Model',
    TolqcCentreRequestSchema.to_model_dict()
)

centre_request_schema = TolqcCentreRequestSchema()
centre_response_schema = TolqcCentreResponseSchema()


class TolqcCentreDetailResource(Resource):
    name = 'centre'

    @centre_namespace.response(
        200,
        description='Success',
        model=centre_response_model,
    )
    @centre_namespace.response(
        404,
        description='Not Found'
    )
    def get(self, id):
        centre = centre_response_schema.get_by_id(id)
        if centre is None:
            # TODO make a custom error response in class
            return {
                "error": f"Centre with id {id} not found"
            }, 404
        return centre, 200


class TolqcCentreListResource(Resource):
    name = 'centres'

    @centre_namespace.expect(centre_request_model)
    @centre_namespace.response(
        200,
        description='Success',
        model=centre_response_model,
    )
    @centre_namespace.response(
        400,
        description='Error'
    )
    def post(self):
        data = centre_namespace.payload
        return centre_response_schema.dump(
            centre_request_schema.save_and_get_model(
                data
            )
        ), 200


centre_namespace.add_resource(TolqcCentreDetailResource, '/<int:id>')
centre_namespace.add_resource(TolqcCentreListResource, '')
