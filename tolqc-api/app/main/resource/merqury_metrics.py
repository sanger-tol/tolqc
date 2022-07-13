# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import MerquryMetricsService
from main.swagger import MerquryMetricsSwagger

from .base import AutoResourceGroup, setup_resource


api_merqury_metrics = MerquryMetricsSwagger.api


@setup_resource
class MerquryMetricsResource(AutoResourceGroup):
    class Meta:
        service = MerquryMetricsService
        swagger = MerquryMetricsSwagger
