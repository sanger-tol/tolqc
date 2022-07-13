# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Resource as FlaskRestxResource

from main.resource.base import BaseResource, setup_resource

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


@setup_resource
class A_Resource(BaseResource):
    class Meta:
        service = A_Service
        swagger = A_Swagger


@setup_resource
class B_Resource(BaseResource):
    class Meta:
        service = B_Service
        swagger = B_Swagger


@setup_resource
class C_Resource(BaseResource):
    class Meta:
        service = C_Service
        swagger = C_Swagger


@setup_resource
class D_Resource(BaseResource):
    class Meta:
        service = D_Service
        swagger = D_Swagger


@setup_resource
class E_Resource(BaseResource):
    class Meta:
        service = E_Service
        swagger = E_Swagger


@setup_resource
class F_Resource(BaseResource):
    class Meta:
        service = F_Service
        swagger = F_Swagger


@setup_resource
class G_Resource(BaseResource):
    class Meta:
        service = G_Service
        swagger = G_Swagger


@setup_resource
class H_Resource(BaseResource):
    class Meta:
        service = H_Service
        swagger = H_Swagger
    
    @api_H.route('/42')
    class H_42Resource(FlaskRestxResource):
        @classmethod
        def get(cls):
            return H_Service.return_42()


@setup_resource
class I_Resource(BaseResource):
    class Meta:
        service = I_Service
        swagger = I_Swagger


@setup_resource
class J_Resource(BaseResource):
    class Meta:
        service = J_Service
        swagger = J_Swagger
