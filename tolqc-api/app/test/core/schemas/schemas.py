# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema.base import BaseDetailRequestSchema, \
                             BaseDetailResponseSchema, \
                             BaseListRequestSchema, \
                             BaseListResponseSchema, \
                             BaseMeta

from test.core.models import ModelRelationshipB, \
                             ModelWithNullableColumn, \
                             ModelWithNonNullableColumn, \
                             ModelWithExtField


class BMeta(BaseMeta):
    type_ = 'B'
    model = ModelRelationshipB


class B_DetailRequestSchema(BaseDetailRequestSchema):
    Meta = BMeta


class B_DetailResponseSchema(BaseDetailResponseSchema):
    Meta = BMeta


class B_ListRequestSchema(BaseListRequestSchema):
    Meta = BMeta


class B_ListResponseSchema(BaseListResponseSchema):
    Meta = BMeta


class CMeta(BaseMeta):
    type_ = 'C'
    model = ModelWithNullableColumn


class C_DetailRequestSchema(BaseDetailRequestSchema):
    Meta = CMeta


class C_DetailResponseSchema(BaseDetailResponseSchema):
    Meta = CMeta


class C_ListRequestSchema(BaseListRequestSchema):
    Meta = CMeta


class C_ListResponseSchema(BaseListResponseSchema):
    Meta = CMeta


class DMeta(BaseMeta):
    type_ = 'D'
    model = ModelWithNonNullableColumn


class D_DetailRequestSchema(BaseDetailRequestSchema):
    Meta = DMeta


class D_DetailResponseSchema(BaseDetailResponseSchema):
    Meta = DMeta


class D_ListRequestSchema(BaseListRequestSchema):
    Meta = DMeta


class D_ListResponseSchema(BaseListResponseSchema):
    Meta = DMeta


class FMeta(BaseMeta):
    type_ = 'F'
    model = ModelWithExtField


class F_DetailRequestSchema(BaseDetailRequestSchema):
    Meta = FMeta


class F_DetailResponseSchema(BaseDetailResponseSchema):
    Meta = FMeta


class F_ListRequestSchema(BaseListRequestSchema):
    Meta = FMeta


class F_ListResponseSchema(BaseListResponseSchema):
    Meta = FMeta
