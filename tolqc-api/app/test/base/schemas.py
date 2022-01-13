# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from marshmallow_jsonapi.fields import Relationship

from main.schema.base import BaseSchema, setup_schema

from test.base.models import B_ModelRelationship, \
                             C_ModelWithNullableColumn, \
                             D_ModelWithNonNullableColumn, \
                             F_ModelWithExtField


class B_Meta(BaseSchema.BaseMeta):
    type_ = 'B'
    model = B_ModelRelationship


@setup_schema
class B_Schema(BaseSchema):
    Meta = B_Meta
    # TODO make resources dynamically generated for related urls
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
