# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import BaseNamespace, BaseDetailResource, \
                  BaseListResource
from main.schema import CentreDetailSchema, \
                        CentreListSchema

centre_namespace = BaseNamespace(
    'centres',
    description='Centre related methods',
)

centre_detail_response_model = centre_namespace.schema_model(
    'Centre Individual Response',
    CentreDetailSchema.to_schema_model_dict()
)

centre_post_request_model = centre_namespace.schema_model(
    'Centre POST Request',
    CentreListSchema.to_post_schema_model_dict()
)

centre_put_model = centre_namespace.model(
    'Centre PUT Request',
    CentreDetailSchema.to_put_model_dict()
)

centre_list_response_model = centre_namespace.schema_model(
    'Centre Bulk Response',
    CentreListSchema.to_schema_model_dict()
)

class TolqcCentreDetailResource(BaseDetailResource):
    name = 'centre'
    namespace = centre_namespace
    schema = CentreDetailSchema()

    @centre_namespace.response(
        200,
        description='Success',
        model=centre_detail_response_model,
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
    def delete(self, id):
        return self._delete_by_id(id)

    @centre_namespace.expect(centre_put_model)
    @centre_namespace.response(
        200,
        description='Success',
        model=centre_detail_response_model
    )
    @centre_namespace.response(
        400,
        description='Bad Request'
    )
    @centre_namespace.response(
        404,
        description='Not Found'
    )
    def put(self, id):
        return self._put_by_id(id)


class TolqcCentreListResource(BaseListResource):
    name = 'centres'
    namespace = centre_namespace
    schema = CentreListSchema()

    @centre_namespace.expect(centre_post_request_model)
    @centre_namespace.response(
        200,
        description='Success',
        model=centre_list_response_model,
    )
    @centre_namespace.response(
        400,
        description='Error'
    )
    def post(self):
        return self._post()
    
    @centre_namespace.response(
        200,
        description='Success',
        model=centre_list_response_model
    )
    def get(self):
        pass


centre_namespace.add_resource(TolqcCentreDetailResource, '/<int:id>')
centre_namespace.add_resource(TolqcCentreListResource, '')
