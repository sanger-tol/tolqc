# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.swagger.base import BaseSwagger, setup_swagger

from test.base.schemas import A_Schema, B_Schema, C_Schema, \
                              D_Schema, E_Schema, F_Schema, \
                              G_Schema, H_Schema


@setup_swagger
class A_Swagger(BaseSwagger):
    class Meta:
        schema = A_Schema


@setup_swagger
class B_Swagger(BaseSwagger):
    class Meta:
        schema = B_Schema


@setup_swagger
class C_Swagger(BaseSwagger):
    class Meta:
        schema = C_Schema


@setup_swagger
class D_Swagger(BaseSwagger):
    class Meta:
        schema = D_Schema


@setup_swagger
class E_Swagger(BaseSwagger):
    class Meta:
        schema = E_Schema


@setup_swagger
class F_Swagger(BaseSwagger):
    class Meta:
        schema = F_Schema


@setup_swagger
class G_Swagger(BaseSwagger):
    class Meta:
        schema = G_Schema


@setup_swagger
class H_Swagger(BaseSwagger):
    class Meta:
        schema = H_Schema
