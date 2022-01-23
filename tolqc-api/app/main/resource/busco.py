# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import BuscoService
from main.swagger import BuscoSwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_busco = BuscoSwagger.api


class BuscoResourceMeta:
    service = BuscoService
    swagger = BuscoSwagger


@setup_resource
class BuscoDetailResource(BaseDetailResource):
    Meta = BuscoResourceMeta


@setup_resource
class BuscoListResource(BaseListResource):
    Meta = BuscoResourceMeta
