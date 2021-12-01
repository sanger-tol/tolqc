# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema.base import BaseRequestSchema, \
                             BaseResponseSchema

from test.core.models import ModelRelationshipB, \
                             ModelWithNullableColumn, \
                             ModelWithNonNullableColumn


class B_RequestSchema(BaseRequestSchema):
    class Meta:
        type_ = 'B'
        strict = True
        model = ModelRelationshipB


class B_ResponseSchema(BaseResponseSchema):
    class Meta:
        type_ = 'B'
        strict = True
        model = ModelRelationshipB


class C_RequestSchema(BaseRequestSchema):
    class Meta:
        type_ = 'C'
        strict = True
        model = ModelWithNullableColumn


class C_ResponseSchema(BaseResponseSchema):
    class Meta:
        type_ = 'C'
        strict = True
        model = ModelWithNullableColumn


class D_RequestSchema(BaseRequestSchema):
    class Meta:
        type_ = 'D'
        strict = True
        model = ModelWithNonNullableColumn


class D_ResponseSchema(BaseResponseSchema):
    class Meta:
        type_ = 'D'
        strict = True
        model = ModelWithNonNullableColumn
