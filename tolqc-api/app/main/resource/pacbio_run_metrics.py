# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import PacbioRunMetricsService
from main.swagger import PacbioRunMetricsSwagger
from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_pacbio_run_metrics = PacbioRunMetricsSwagger.api


@setup_resource_group
class PacbioRunMetricsResourceGroup(AutoResourceGroup):
    class Meta:
        service = PacbioRunMetricsService
        swagger = PacbioRunMetricsSwagger
