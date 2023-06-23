# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import ContigvizMetricsService
from main.swagger import ContigvizMetricsSwagger
from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_contigviz_metrics = ContigvizMetricsSwagger.api


@setup_resource_group
class ContigvizMetricsResourceGroup(AutoResourceGroup):
    class Meta:
        service = ContigvizMetricsService
        swagger = ContigvizMetricsSwagger
