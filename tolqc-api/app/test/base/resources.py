# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.auth import auth

from main.resource.base import AutoResourceGroup, BaseResource, setup_resource_group

from test.base.services import A_Service, B_Service, C_Service, D_Service, \
                               E_Service, F_Service, G_Service, H_Service, \
                               I_Service, J_Service
from test.base.swaggers import A_Swagger, B_Swagger, C_Swagger, D_Swagger, \
                               E_Swagger, F_Swagger, G_Swagger, H_Swagger, \
                               I_Swagger, J_Swagger


api_A = A_Swagger.api
api_B = B_Swagger.api
api_C = C_Swagger.api
api_D = D_Swagger.api
api_E = E_Swagger.api
api_F = F_Swagger.api
api_G = G_Swagger.api
api_H = H_Swagger.api
api_I = I_Swagger.api
api_J = J_Swagger.api


@setup_resource_group
class A_Resource(AutoResourceGroup):
    class Meta:
        service = A_Service
        swagger = A_Swagger


@setup_resource_group
class B_Resource(AutoResourceGroup):
    class Meta:
        service = B_Service
        swagger = B_Swagger


@setup_resource_group
class C_Resource(AutoResourceGroup):
    class Meta:
        service = C_Service
        swagger = C_Swagger


@setup_resource_group
class D_Resource(AutoResourceGroup):
    class Meta:
        service = D_Service
        swagger = D_Swagger


@setup_resource_group
class E_Resource(AutoResourceGroup):
    class Meta:
        service = E_Service
        swagger = E_Swagger


@setup_resource_group
class F_Resource(AutoResourceGroup):
    class Meta:
        service = F_Service
        swagger = F_Swagger


@setup_resource_group
class G_Resource(AutoResourceGroup):
    class Meta:
        service = G_Service
        swagger = G_Swagger


@setup_resource_group
class H_Resource(AutoResourceGroup):
    class Meta:
        service = H_Service
        swagger = H_Swagger

    @api_H.route('/42')
    class H_42Resource(BaseResource):
        @classmethod
        def get(cls):
            return H_Service.return_42()


@setup_resource_group
class I_Resource(AutoResourceGroup):
    class Meta:
        service = I_Service
        swagger = I_Swagger

    @api_I.route('/parrot')
    class I_ParrotResouce(BaseResource):
        @classmethod
        @auth(api_I)
        def post(cls, user_id=None):
            return I_Service.parrot(user_id=user_id)


@setup_resource_group
class J_Resource(AutoResourceGroup):
    class Meta:
        service = J_Service
        swagger = J_Swagger
