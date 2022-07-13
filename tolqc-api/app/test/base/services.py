# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service.base import BaseService, setup_service

from test.base.models import A_ModelRelationship, \
                             B_ModelRelationship, \
                             C_ModelWithNullableColumn, \
                             D_ModelWithNonNullableColumn, \
                             E_ModelRelationship, \
                             F_ModelWithExtField, \
                             G_ModelWithFilterableFields, \
                             H_ModelLog, \
                             I_ModelEnum, \
                             J_ModelEnumDependent
from test.base.schemas import A_Schema, B_Schema, C_Schema, \
                              D_Schema, E_Schema, F_Schema, \
                              G_Schema, H_Schema, I_Schema, \
                              J_Schema


@setup_service
class A_Service(BaseService):
    class Meta:
        model = A_ModelRelationship
        schema = A_Schema


@setup_service
class B_Service(BaseService):
    class Meta:
        model = B_ModelRelationship
        schema = B_Schema


@setup_service
class C_Service(BaseService):
    class Meta:
        model = C_ModelWithNullableColumn
        schema = C_Schema


@setup_service
class D_Service(BaseService):
    class Meta:
        model = D_ModelWithNonNullableColumn
        schema = D_Schema


@setup_service
class E_Service(BaseService):
    class Meta:
        model = E_ModelRelationship
        schema = E_Schema


@setup_service
class F_Service(BaseService):
    class Meta:
        model = F_ModelWithExtField
        schema = F_Schema


@setup_service
class G_Service(BaseService):
    class Meta:
        model = G_ModelWithFilterableFields
        schema = G_Schema


@setup_service
class H_Service(BaseService):
    class Meta:
        model = H_ModelLog
        schema = H_Schema

    def return_42():
        return {'data': 42}, 200


@setup_service
class I_Service(BaseService):
    class Meta:
        model = I_ModelEnum
        schema = I_Schema


@setup_service
class J_Service(BaseService):
    class Meta:
        model = J_ModelEnumDependent
        schema = J_Schema
