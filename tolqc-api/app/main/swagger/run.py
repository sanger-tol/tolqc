# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.resource.base import BaseNamespace, BaseDetailResource, \
                  BaseListResource
from main.schema import RunListSchema, \
                        RunDetailSchema
from main.auth import auth


run_namespace = BaseNamespace(
    'runs',
    description='ToLQC-Run related methods',
)

run_detail_response_model = run_namespace.schema_model(
    'Run Individual Response',
    RunDetailSchema.to_response_schema_model_dict()
)

run_post_request_model = run_namespace.schema_model(
    'Run POST Request',
    RunListSchema.to_post_request_schema_model_dict()
)

run_put_request_model = run_namespace.model(
    'Run PUT Request',
    RunDetailSchema.to_put_request_model_dict()
)

run_list_response_model = run_namespace.schema_model(
    'Run Bulk Response',
    RunListSchema.to_response_schema_model_dict()
)


class TolqcRunDetailResource(BaseDetailResource):
    name = "run"
    namespace = run_namespace
    schema = RunDetailSchema()

    @run_namespace.response(
        200,
        'Success',
        run_detail_response_model
    )
    @run_namespace.response(
        404,
        'Not Found'
    )
    def get(self, id):
        return self._get_by_id(id)

    @run_namespace.expect(run_put_request_model)
    @run_namespace.response(
        200,
        'Success',
        run_detail_response_model
    )
    @run_namespace.response(
        400,
        'Bad Request'
    )
    @run_namespace.response(
        404,
        'Not Found'
    )
    @auth(run_namespace)
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
    @auth(run_namespace)
    def delete(self, id):
        return self._delete_by_id(id)


class TolqcRunListResource(BaseListResource):
    name = "runs"
    namespace = run_namespace
    schema = RunListSchema()

    @run_namespace.expect(run_post_request_model)
    @run_namespace.response(
        200,
        description='Success',
        model=run_list_response_model,
    )
    @run_namespace.response(
        400,
        description='Bad Request'
    )
    @auth(run_namespace)
    def post(self):
        return self._post()

    @run_namespace.response(
        200,
        description='Success',
        model=run_list_response_model,
    )
    def get(self):
        return self._get()


run_namespace.add_resource(TolqcRunDetailResource, '/<int:id>')
run_namespace.add_resource(TolqcRunListResource, '')
