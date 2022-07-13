# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import GenomescopeMetricsService
from main.swagger import GenomescopeMetricsSwagger

from .base import AutoResourceGroup, setup_resource_group


api_genomescope_metrics = GenomescopeMetricsSwagger.api


@setup_resource_group
class GenomescopeMetricsResourceGroup(AutoResourceGroup):
    class Meta:
        service = GenomescopeMetricsService
        swagger = GenomescopeMetricsSwagger
