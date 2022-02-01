# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema.base import BaseSchema, setup_schema

from test.base.models import A_ModelRelationship, \
                             B_ModelRelationship, \
                             C_ModelWithNullableColumn, \
                             D_ModelWithNonNullableColumn, \
                             E_ModelRelationship, \
                             F_ModelWithExtField, \
                             G_ModelWithFilterableFields, \
                             H_ModelLog, \
                             I_ModelEnum


@setup_schema
class A_Schema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = A_ModelRelationship


@setup_schema
class B_Schema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = B_ModelRelationship


@setup_schema
class C_Schema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = C_ModelWithNullableColumn


@setup_schema
class D_Schema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = D_ModelWithNonNullableColumn


@setup_schema
class E_Schema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = E_ModelRelationship


@setup_schema
class F_Schema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = F_ModelWithExtField


@setup_schema
class G_Schema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = G_ModelWithFilterableFields


@setup_schema
class H_Schema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = H_ModelLog


@setup_schema
class I_Schema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = I_ModelEnum
