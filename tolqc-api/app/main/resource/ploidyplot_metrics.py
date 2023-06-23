# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import PloidyplotMetricsService
from main.swagger import PloidyplotMetricsSwagger
from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_ploidyplot_metrics = PloidyplotMetricsSwagger.api


@setup_resource_group
class PloidyplotMetricsResourceGroup(AutoResourceGroup):
    class Meta:
        service = PloidyplotMetricsService
        swagger = PloidyplotMetricsSwagger
