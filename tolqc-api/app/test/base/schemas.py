# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema.base import BaseSchema, BaseMeta, \
                             BaseSchema, BaseMeta, \
                             setup_schema

from test.base.models import ModelRelationshipB, \
                             ModelWithNullableColumn, \
                             ModelWithNonNullableColumn, \
                             ModelWithExtField


class B_Meta(BaseMeta):
    type_ = 'B'
    model = ModelRelationshipB


@setup_schema
class B_Schema(BaseSchema):
    Meta = B_Meta


class C_Meta(BaseMeta):
    type_ = 'C'
    model = ModelWithNullableColumn


@setup_schema
class C_Schema(BaseSchema):
    Meta = C_Meta


class D_Meta(BaseMeta):
    type_ = 'D'
    model = ModelWithNonNullableColumn


@setup_schema
class D_Schema(BaseSchema):
    Meta = D_Meta


class F_Meta(BaseMeta):
    type_ = 'F'
    model = ModelWithExtField


@setup_schema
class F_Schema(BaseSchema):
    Meta = F_Meta
