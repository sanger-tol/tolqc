# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import GenomescopeMetricsService
from main.swagger import GenomescopeMetricsSwagger

from .base import BaseResource, setup_resource


api_genomescope_metrics = GenomescopeMetricsSwagger.api


@setup_resource
class GenomescopeMetricsResource(BaseResource):
    class Meta:
        service = GenomescopeMetricsService
        swagger = GenomescopeMetricsSwagger
