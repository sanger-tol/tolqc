# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from marshmallow_jsonapi.fields import Relationship

from main.schema.base import BaseSchema, setup_schema

from test.base.models import A_ModelRelationship, \
                             B_ModelRelationship, \
                             C_ModelWithNullableColumn, \
                             D_ModelWithNonNullableColumn, \
                             F_ModelWithExtField, \
                             E_ModelRelationship


class A_Meta(BaseSchema.BaseMeta):
    type_ = 'A'
    model = A_ModelRelationship


@setup_schema
class A_Schema(BaseSchema):
    Meta = A_Meta


class B_Meta(BaseSchema.BaseMeta):
    type_ = 'B'
    model = B_ModelRelationship
    # this below needs to be in the constructor
    #exclude=('a_id',)


@setup_schema
class B_Schema(BaseSchema):
    Meta = B_Meta

    # everything below this needs to be dynamic, on BaseSchema
    # this is just to get an understanding!!!!
    # A = Relationship(
    #     '/A/{id}',
    #     related_url_kwargs={'id': '<a_id>'},
    #     include_resource_linkage=True,
    #     type_='A',
    #     attribute='a_id'
    # )
    E = Relationship(
        '/B/{id}/E',
        related_url_kwargs={'id': '<id>'},
        many=True,
        type_='E',
        dump_default=lambda: []
    )


class C_Meta(BaseSchema.BaseMeta):
    type_ = 'C'
    model = C_ModelWithNullableColumn


@setup_schema
class C_Schema(BaseSchema):
    Meta = C_Meta


class D_Meta(BaseSchema.BaseMeta):
    type_ = 'D'
    model = D_ModelWithNonNullableColumn


@setup_schema
class D_Schema(BaseSchema):
    Meta = D_Meta


class F_Meta(BaseSchema.BaseMeta):
    type_ = 'F'
    model = F_ModelWithExtField


@setup_schema
class F_Schema(BaseSchema):
    Meta = F_Meta
