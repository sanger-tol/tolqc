# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service.base import BaseService

from test.base.models import A_ModelRelationship, \
                             B_ModelRelationship, \
                             C_ModelWithNullableColumn, \
                             D_ModelWithNonNullableColumn, \
                             E_ModelRelationship, \
                             F_ModelWithExtField, \
                             G_ModelWithFilterableFields
from test.base.schemas import A_Schema, B_Schema, C_Schema, \
                              D_Schema, E_Schema, F_Schema, \
                              G_Schema


class A_Service(BaseService):
    class Meta:
        model = A_ModelRelationship
        schema = A_Schema


class B_Service(BaseService):
    class Meta:
        model = B_ModelRelationship
        schema = B_Schema


class C_Service(BaseService):
    class Meta:
        model = C_ModelWithNullableColumn
        schema = C_Schema


class D_Service(BaseService):
    class Meta:
        model = D_ModelWithNonNullableColumn
        schema = D_Schema


class E_Service(BaseService):
    class Meta:
        model = E_ModelRelationship
        schema = E_Schema



class F_Service(BaseService):
    class Meta:
        model = F_ModelWithExtField
        schema = F_Schema


class G_Service(BaseService):
    class Meta:
        model = G_ModelWithFilterableFields
        schema = G_Schema
