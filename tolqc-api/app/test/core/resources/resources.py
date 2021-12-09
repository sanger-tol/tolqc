# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.resource.base import BaseNamespace, \
                               BaseDetailResource, \
                               BaseListResource

from test.core.schemas import B_DetailSchema, \
                              B_ListSchema, \
                              C_DetailSchema, \
                              C_ListSchema, \
                              D_DetailSchema, \
                              D_ListSchema, \
                              F_DetailSchema, \
                              F_ListSchema


b_namespace = BaseNamespace('B')
c_namespace = BaseNamespace('C')
d_namespace = BaseNamespace('D')
f_namespace = BaseNamespace('F')

b_post_model = b_namespace.schema_model(
    'B Post',
    B_ListSchema.to_post_schema_model_dict()
)
b_put_model = b_namespace.model(
    'B put',
    B_DetailSchema.to_put_model_dict()
)
b_response_model = b_namespace.schema_model(
    'B response',
    B_DetailSchema.to_schema_model_dict()
)

c_post_model = c_namespace.schema_model(
    'C Post',
    C_ListSchema.to_post_schema_model_dict()
)
c_put_model = c_namespace.model(
    'C put',
    C_DetailSchema.to_put_model_dict()
)
c_response_model = c_namespace.schema_model(
    'C response',
    C_DetailSchema.to_schema_model_dict()
)

d_post_model = d_namespace.schema_model(
    'D Post',
    D_ListSchema.to_post_schema_model_dict()
)
d_put_model = d_namespace.model(
    'D put',
    D_DetailSchema.to_put_model_dict()
)
d_response_model = d_namespace.schema_model(
    'D response',
    D_DetailSchema.to_schema_model_dict()
)

f_post_model = f_namespace.schema_model(
    'F Post',
    F_ListSchema.to_post_schema_model_dict()
)
f_put_model = f_namespace.model(
    'F put',
    F_DetailSchema.to_put_model_dict()
)
f_response_model = f_namespace.schema_model(
    'F response',
    F_DetailSchema.to_schema_model_dict()
)


class B_DetailResource(BaseDetailResource):
    name = 'B'
    namespace = b_namespace
    schema = B_DetailSchema()

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
    schema = B_ListSchema()

    @b_namespace.expect(b_post_model)
    def post(self):
        return self._post()


class C_DetailResource(BaseDetailResource):
    name = 'C'
    namespace = c_namespace
    schema = C_DetailSchema()

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
    schema = C_ListSchema()

    @c_namespace.expect(c_post_model)
    def post(self):
        return self._post()


class D_DetailResource(BaseDetailResource):
    name = 'D'
    namespace = d_namespace
    schema = D_DetailSchema()

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
    schema = D_ListSchema()

    @d_namespace.expect(d_post_model)
    def post(self):
        return self._post()


class F_DetailResource(BaseDetailResource):
    name = 'F'
    namespace = f_namespace
    schema = F_DetailSchema()

    def get(self, id):
        return self._get_by_id(id)

    @f_namespace.expect(f_put_model)
    def put(self, id):
        return self._put_by_id(id)

    def delete(self, id):
        return self._delete_by_id(id)


class F_ListResource(BaseListResource):
    name = 'F'
    namespace = f_namespace
    schema = F_ListSchema()

    @f_namespace.expect(f_post_model)
    def post(self):
        return self._post()


b_namespace.add_resource(B_DetailResource, '/<int:id>')
b_namespace.add_resource(B_ListResource, '')

c_namespace.add_resource(C_DetailResource, '/<int:id>')
c_namespace.add_resource(C_ListResource, '')

d_namespace.add_resource(D_DetailResource, '/<int:id>')
d_namespace.add_resource(D_ListResource, '')

f_namespace.add_resource(F_DetailResource, '/<int:id>')
f_namespace.add_resource(F_ListResource, '')
