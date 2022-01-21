# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import AsmService
from main.swagger import AsmSwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_Asm = AsmSwagger.api


class AsmResourceMeta:
    service = AsmService
    swagger = AsmSwagger


@setup_resource
class AsmDetailResource(BaseDetailResource):
    Meta = AsmResourceMeta


@setup_resource
class AsmListResource(BaseListResource):
    Meta = AsmResourceMeta
