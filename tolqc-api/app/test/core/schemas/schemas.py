# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema.base import BaseRequestSchema, \
                             BaseResponseSchema, \
                             BaseMeta

from test.core.models import ModelRelationshipB, \
                             ModelWithNullableColumn, \
                             ModelWithNonNullableColumn, \
                             ModelWithExtField

class BMeta(BaseMeta):
    type_ = 'B'
    model = ModelRelationshipB


class B_RequestSchema(BaseRequestSchema):
    Meta = BMeta
        

class B_ResponseSchema(BaseResponseSchema):
    Meta = BMeta


class CMeta(BaseMeta):
    type_ = 'C'
    model = ModelWithNullableColumn


class C_RequestSchema(BaseRequestSchema):
    Meta = CMeta


class C_ResponseSchema(BaseResponseSchema):
    Meta = CMeta


class DMeta(BaseMeta):
    type_ = 'D'
    model = ModelWithNonNullableColumn


class D_RequestSchema(BaseRequestSchema):
    Meta = DMeta


class D_ResponseSchema(BaseResponseSchema):
    Meta = DMeta


class FMeta(BaseMeta):
    type_ = 'F'
    model = ModelWithExtField


class F_RequestSchema(BaseRequestSchema):
    Meta = FMeta


class F_ResponseSchema(BaseResponseSchema):
    Meta = FMeta
