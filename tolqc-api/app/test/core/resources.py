# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.resource.base import BaseNamespace, \
                               BaseDetailResource, \
                               BaseListResource

from test.core.schemas import B_RequestSchema, \
                              B_ResponseSchema, \
                              C_RequestSchema, \
                              C_ResponseSchema, \
                              D_RequestSchema, \
                              D_ResponseSchema


b_namespace = BaseNamespace('B')
c_namespace = BaseNamespace('C')
d_namespace = BaseNamespace('D')

b_post_model = b_namespace.model(
    'B Post',
    B_RequestSchema.to_post_model_dict()
)
b_put_model = b_namespace.model(
    'B put',
    B_RequestSchema.to_put_model_dict()
)
b_response_model = b_namespace.schema_model(
    'B response',
    B_ResponseSchema.to_schema_model_dict()
)

c_post_model = c_namespace.model(
    'C Post',
    C_RequestSchema.to_post_model_dict()
)
c_put_model = c_namespace.model(
    'C put',
    C_RequestSchema.to_put_model_dict()
)
c_response_model = c_namespace.schema_model(
    'C response',
    C_ResponseSchema.to_schema_model_dict()
)

d_post_model = d_namespace.model(
    'D Post',
    D_RequestSchema.to_post_model_dict()
)
d_put_model = d_namespace.model(
    'D put',
    D_RequestSchema.to_put_model_dict()
)
d_response_model = d_namespace.schema_model(
    'D response',
    D_ResponseSchema.to_schema_model_dict()
)


class B_DetailResource(BaseDetailResource):
    name = 'B'
    namespace = b_namespace
    request_schema = B_RequestSchema()
    response_schema = B_ResponseSchema()

    def get(self, id):
        return self._get_by_id(id)
    
    @b_namespace.expect(b_put_model)
    def put(self, id):
        return self._put_by_id(id)
    
    def delete(self, id):
        return self._delete_by_id(id)


class B_ListResource(BaseListResource):
    name = 'B'
    namespace = b_namespace
    request_schema = B_RequestSchema()
    response_schema = B_ResponseSchema()

    @b_namespace.expect(b_post_model)
    def post(self):
        return self._post()


class C_DetailResource(BaseDetailResource):
    name = 'C'
    namespace = c_namespace
    request_schema = C_RequestSchema()
    response_schema = C_ResponseSchema()

    def get(self, id):
        return self._get_by_id(id)
    
    @c_namespace.expect(c_put_model)
    def put(self, id):
        return self._put_by_id(id)
    
    def delete(self, id):
        return self._delete_by_id(id)


class C_ListResource(BaseListResource):
    name = 'C'
    namespace = c_namespace
    request_schema = C_RequestSchema()
    response_schema = C_ResponseSchema()

    @c_namespace.expect(c_post_model)
    def post(self):
        return self._post()


class D_DetailResource(BaseDetailResource):
    name = 'D'
    namespace = d_namespace
    request_schema = D_RequestSchema()
    response_schema = D_ResponseSchema()

    def get(self, id):
        return self._get_by_id(id)
    
    @d_namespace.expect(d_put_model)
    def put(self, id):
        return self._put_by_id(id)
    
    def delete(self, id):
        return self._delete_by_id(id)


class D_ListResource(BaseListResource):
    name = 'D'
    namespace = d_namespace
    request_schema = D_RequestSchema()
    response_schema = D_ResponseSchema()

    @d_namespace.expect(d_post_model)
    def post(self):
        return self._post()


b_namespace.add_resource(B_DetailResource, '/<int:id>')
b_namespace.add_resource(B_ListResource, '')

c_namespace.add_resource(C_DetailResource, '/<int:id>')
c_namespace.add_resource(C_ListResource, '')

d_namespace.add_resource(D_DetailResource, '/<int:id>')
d_namespace.add_resource(D_ListResource, '')
