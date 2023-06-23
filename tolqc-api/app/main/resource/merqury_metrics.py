# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import MerquryMetricsService
from main.swagger import MerquryMetricsSwagger
from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_merqury_metrics = MerquryMetricsSwagger.api


@setup_resource_group
class MerquryMetricsResourceGroup(AutoResourceGroup):
    class Meta:
        service = MerquryMetricsService
        swagger = MerquryMetricsSwagger
