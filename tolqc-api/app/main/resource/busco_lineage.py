# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import BuscoLineageService
from main.swagger import BuscoLineageSwagger

from .base import AutoResourceGroup, setup_resource_group


api_busco_lineage = BuscoLineageSwagger.api


@setup_resource_group
class BuscoLineageResourceGroup(AutoResourceGroup):
    class Meta:
        service = BuscoLineageService
        swagger = BuscoLineageSwagger
