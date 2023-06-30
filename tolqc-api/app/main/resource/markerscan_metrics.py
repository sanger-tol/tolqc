# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import MarkerscanMetricsService
from main.swagger import MarkerscanMetricsSwagger

from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_markerscan_metrics = MarkerscanMetricsSwagger.api


@setup_resource_group
class MarkerscanMetricsResourceGroup(AutoResourceGroup):
    class Meta:
        service = MarkerscanMetricsService
        swagger = MarkerscanMetricsSwagger
