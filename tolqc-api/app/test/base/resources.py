# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.resource.base import BaseResource, setup_resource

from test.base.services import B_Service, C_Service, D_Service, F_Service, G_Service
from test.base.swaggers import B_Swagger, C_Swagger, D_Swagger, F_Swagger, G_Swagger


api_B = B_Swagger.api
api_C = C_Swagger.api
api_D = D_Swagger.api
api_F = F_Swagger.api
api_G = G_Swagger.api


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
class F_Resource(BaseResource):
    class Meta:
        service = F_Service
        swagger = F_Swagger


@setup_resource
class G_Resource(BaseResource):
    class Meta:    
        service = G_Service
        swagger = G_Swagger
