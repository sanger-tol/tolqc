# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import BaseNamespace, BaseDetailResource, \
                  BaseListResource
from main.schema import TolqcRunRequestSchema, \
                        TolqcRunResponseSchema


run_namespace = BaseNamespace(
    'runs',
    description='ToLQC-Run related methods',
)

run_response_model = run_namespace.schema_model(
    'Run Response',
    TolqcRunResponseSchema.to_schema_model_dict()
)

run_post_model = run_namespace.model(
    'Run POST Request',
    TolqcRunRequestSchema.to_post_model_dict()
)

run_put_model = run_namespace.model(
    'Run PUT Request',
    TolqcRunRequestSchema.to_put_model_dict()
)


class TolqcRunDetailResource(BaseDetailResource):
    name = "run"
    namespace = run_namespace
    request_schema = TolqcRunRequestSchema()
    response_schema = TolqcRunResponseSchema()

    @run_namespace.response(
        200,
        'Success',
        run_response_model
    )
    @run_namespace.response(
        404,
        'Not Found'
    )
    def get(self, id):
        return self._get_by_id(id)

    @run_namespace.expect(run_put_model)
    @run_namespace.response(
        200,
        'Success',
        run_response_model
    )
    @run_namespace.response(
        400,
        'Bad Request'
    )
    @run_namespace.response(
        404,
        'Not Found'
    )
    def put(self, id):
        return self._put_by_id(id)

    @run_namespace.response(
        204,
        'Success'
    )
    @run_namespace.response(
        400,
        'Bad Request'
    )
    @run_namespace.response(
        404,
        'Not Found'
    )
    def delete(self, id):
        return self._delete_by_id(id)


class TolqcRunListResource(BaseListResource):
    name = "runs"
    namespace = run_namespace
    request_schema = TolqcRunRequestSchema()
    response_schema = TolqcRunResponseSchema()

    @run_namespace.expect(run_post_model)
    @run_namespace.response(
        200,
        description='Success',
        model=run_response_model,
    )
    @run_namespace.response(
        400,
        description='Bad Request'
    )
    def post(self):
        return self._post()


run_namespace.add_resource(TolqcRunDetailResource, '/<int:id>')
run_namespace.add_resource(TolqcRunListResource, '')
