# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import BuscoLineageService
from main.swagger import BuscoLineageSwagger

from .base import AutoResourceGroup, setup_resource


api_busco_lineage = BuscoLineageSwagger.api


@setup_resource
class BuscoLineageResource(AutoResourceGroup):
    class Meta:
        service = BuscoLineageService
        swagger = BuscoLineageSwagger
