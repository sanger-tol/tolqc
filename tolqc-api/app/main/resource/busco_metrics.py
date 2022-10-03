# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import BuscoMetricsService
from main.swagger import BuscoMetricsSwagger

from .tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_busco_metrics = BuscoMetricsSwagger.api


@setup_resource_group
class BuscoMetricsResourceGroup(AutoResourceGroup):
    class Meta:
        service = BuscoMetricsService
        swagger = BuscoMetricsSwagger
