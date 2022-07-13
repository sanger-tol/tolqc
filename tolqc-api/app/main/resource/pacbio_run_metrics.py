# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import PacbioRunMetricsService
from main.swagger import PacbioRunMetricsSwagger

from .base import AutoResourceGroup, setup_resource


api_pacbio_run_metrics = PacbioRunMetricsSwagger.api


@setup_resource
class PacbioRunMetricsResource(AutoResourceGroup):
    class Meta:
        service = PacbioRunMetricsService
        swagger = PacbioRunMetricsSwagger
