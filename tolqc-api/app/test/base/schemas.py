# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema.base import BaseSchema, setup_schema

from test.base.models import ModelRelationshipB, \
                             ModelWithNullableColumnC, \
                             ModelWithNonNullableColumnD, \
                             ModelWithExtFieldF


class B_Meta(BaseSchema.BaseMeta):
    type_ = 'B'
    model = ModelRelationshipB


@setup_schema
class B_Schema(BaseSchema):
    Meta = B_Meta


class C_Meta(BaseSchema.BaseMeta):
    type_ = 'C'
    model = ModelWithNullableColumnC


@setup_schema
class C_Schema(BaseSchema):
    Meta = C_Meta


class D_Meta(BaseSchema.BaseMeta):
    type_ = 'D'
    model = ModelWithNonNullableColumnD


@setup_schema
class D_Schema(BaseSchema):
    Meta = D_Meta


class F_Meta(BaseSchema.BaseMeta):
    type_ = 'F'
    model = ModelWithExtFieldF


@setup_schema
class F_Schema(BaseSchema):
    Meta = F_Meta
