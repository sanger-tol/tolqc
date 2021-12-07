# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema.base import BaseDetailRequestSchema, \
                             BaseDetailResponseSchema, \
                             BaseMeta

from test.core.models import ModelRelationshipB, \
                             ModelWithNullableColumn, \
                             ModelWithNonNullableColumn, \
                             ModelWithExtField

class BMeta(BaseMeta):
    type_ = 'B'
    model = ModelRelationshipB


class B_RequestSchema(BaseDetailRequestSchema):
    Meta = BMeta
        

class B_ResponseSchema(BaseDetailResponseSchema):
    Meta = BMeta


class CMeta(BaseMeta):
    type_ = 'C'
    model = ModelWithNullableColumn


class C_RequestSchema(BaseDetailRequestSchema):
    Meta = CMeta


class C_ResponseSchema(BaseDetailResponseSchema):
    Meta = CMeta


class DMeta(BaseMeta):
    type_ = 'D'
    model = ModelWithNonNullableColumn


class D_RequestSchema(BaseDetailRequestSchema):
    Meta = DMeta


class D_ResponseSchema(BaseDetailResponseSchema):
    Meta = DMeta


class FMeta(BaseMeta):
    type_ = 'F'
    model = ModelWithExtField


class F_RequestSchema(BaseDetailRequestSchema):
    Meta = FMeta


class F_ResponseSchema(BaseDetailResponseSchema):
    Meta = FMeta
