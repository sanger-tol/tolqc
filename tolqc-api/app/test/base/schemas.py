# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema.base import BaseSchema, setup_schema

from test.base.models import B_ModelRelationship, \
                             C_ModelWithNullableColumn, \
                             D_ModelWithNonNullableColumn, \
                             F_ModelWithExtField, \
                             G_ModelWithFilterableFields

@setup_schema
class B_Schema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        type_ = 'B'
        model = B_ModelRelationship


@setup_schema
class C_Schema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        type_ = 'C'
        model = C_ModelWithNullableColumn


@setup_schema
class D_Schema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        type_ = 'D'
        model = D_ModelWithNonNullableColumn


@setup_schema
class F_Schema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        type_ = 'F'
        model = F_ModelWithExtField


@setup_schema
class G_Schema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        type_ = 'G'
        model = G_ModelWithFilterableFields
