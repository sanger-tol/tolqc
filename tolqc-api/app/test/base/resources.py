# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.resource.base import BaseListResource, BaseDetailResource, setup_resource

from test.base.services import B_Service, C_Service, D_Service, F_Service
from test.base.swaggers import B_Swagger, C_Swagger, D_Swagger, F_Swagger


api_B = B_Swagger.api
api_C = C_Swagger.api
api_D = D_Swagger.api
api_F = F_Swagger.api


class B_ResourceMeta:
    service = B_Service
    swagger = B_Swagger


@setup_resource
class B_DetailResource(BaseDetailResource):
    Meta = B_ResourceMeta


@setup_resource
class B_ListResource(BaseListResource):
    Meta = B_ResourceMeta


class C_ResourceMeta:
    service = C_Service
    swagger = C_Swagger


@setup_resource
class C_DetailResource(BaseDetailResource):
    Meta = C_ResourceMeta


@setup_resource
class C_ListResource(BaseListResource):
    Meta = C_ResourceMeta


class D_ResourceMeta:
    service = D_Service
    swagger = D_Swagger


@setup_resource
class D_DetailResource(BaseDetailResource):
    Meta = D_ResourceMeta


@setup_resource
class D_ListResource(BaseListResource):
    Meta = D_ResourceMeta


class F_ResourceMeta:
    service = F_Service
    swagger = F_Swagger


@setup_resource
class F_DetailResource(BaseDetailResource):
    Meta = F_ResourceMeta


@setup_resource
class F_ListResource(BaseListResource):
    Meta = F_ResourceMeta
