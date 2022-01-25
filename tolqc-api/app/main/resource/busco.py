# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import BuscoService
from main.swagger import BuscoSwagger

from .base import BaseResource, setup_resource


api_busco = BuscoSwagger.api


@setup_resource
class BuscoResource(BaseResource):
    class Meta:
        service = BuscoService
        swagger = BuscoSwagger
