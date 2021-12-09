# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import BaseNamespace, BaseDetailResource, \
                  BaseListResource
from main.schema import TolqcCentreRequestSchema, \
                        TolqcCentreResponseSchema
from main.resource.auth import auth


centre_namespace = BaseNamespace(
    'centres',
    description='Centre related methods',
)

centre_response_model = centre_namespace.schema_model(
    'Centre Response',
    TolqcCentreResponseSchema.to_schema_model_dict()
)

centre_post_model = centre_namespace.model(
    'Centre POST Request',
    TolqcCentreRequestSchema.to_post_model_dict()
)

centre_put_model = centre_namespace.model(
    'Centre PUT Request',
    TolqcCentreRequestSchema.to_put_model_dict()
)


class TolqcCentreDetailResource(BaseDetailResource):
    name = 'centre'
    namespace = centre_namespace
    request_schema = TolqcCentreRequestSchema()
    response_schema = TolqcCentreResponseSchema()

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
        return self._get_by_id(id)

    @centre_namespace.response(
        204,
        description='Success'
    )
    @centre_namespace.response(
        404,
        description='Not Found'
    )
    @auth(centre_namespace)
    def delete(self, id, request_data):
        return self._delete_by_id(id)

    @centre_namespace.expect(centre_put_model)
    @centre_namespace.response(
        200,
        description='Success',
        model=centre_response_model
    )
    @centre_namespace.response(
        400,
        description='Bad Request'
    )
    @centre_namespace.response(
        404,
        description='Not Found'
    )
    @auth(centre_namespace)
    def put(self, id, request_data):
        return self._put_by_id(id)


class TolqcCentreListResource(BaseListResource):
    name = 'centres'
    namespace = centre_namespace
    request_schema = TolqcCentreRequestSchema()
    response_schema = TolqcCentreResponseSchema()

    @centre_namespace.expect(centre_post_model)
    @centre_namespace.response(
        200,
        description='Success',
        model=centre_response_model,
    )
    @centre_namespace.response(
        400,
        description='Error'
    )
    @auth(centre_namespace)
    def post(self, request_data):
        return self._post()


centre_namespace.add_resource(TolqcCentreDetailResource, '/<int:id>')
centre_namespace.add_resource(TolqcCentreListResource, '')
