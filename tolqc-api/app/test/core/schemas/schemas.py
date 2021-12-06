# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema.base import BaseRequestSchema, \
                             BaseResponseSchema

from test.core.models import ModelRelationshipB, \
                             ModelWithNullableColumn, \
                             ModelWithNonNullableColumn, \
                             ModelWithExtField


class B_RequestSchema(BaseRequestSchema):
    class Meta:
        type_ = 'B'
        strict = True
        model = ModelRelationshipB
        include_fk = True


class B_ResponseSchema(BaseResponseSchema):
    class Meta:
        type_ = 'B'
        strict = True
        model = ModelRelationshipB
        include_fk = True


class C_RequestSchema(BaseRequestSchema):
    class Meta:
        type_ = 'C'
        strict = True
        model = ModelWithNullableColumn
        include_fk = True


class C_ResponseSchema(BaseResponseSchema):
    class Meta:
        type_ = 'C'
        strict = True
        model = ModelWithNullableColumn
        include_fk = True


class D_RequestSchema(BaseRequestSchema):
    class Meta:
        type_ = 'D'
        strict = True
        model = ModelWithNonNullableColumn
        include_fk = True


class D_ResponseSchema(BaseResponseSchema):
    class Meta:
        type_ = 'D'
        strict = True
        model = ModelWithNonNullableColumn
        include_fk = True

class F_RequestSchema(BaseRequestSchema):
    class Meta:
        type_ = 'F'
        strict = True
        model = ModelWithExtField
        include_fk = True


class F_ResponseSchema(BaseResponseSchema):
    class Meta:
        type_ = 'F'
        strict = True
        model = ModelWithExtField
        include_fk = True
