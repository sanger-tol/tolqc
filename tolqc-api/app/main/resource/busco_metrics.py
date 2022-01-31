# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import BuscoMetricsService
from main.swagger import BuscoMetricsSwagger

from .base import BaseResource, setup_resource


api_busco_metrics = BuscoMetricsSwagger.api


@setup_resource
class BuscoMetricsResource(BaseResource):
    class Meta:
        service = BuscoMetricsService
        swagger = BuscoMetricsSwagger
