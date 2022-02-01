# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcGenomescopeMetrics
from main.schema import GenomescopeMetricsSchema

from .base import BaseService, setup_service


@setup_service
class GenomescopeMetricsService(BaseService):
    class Meta:
        model = TolqcGenomescopeMetrics
        schema = GenomescopeMetricsSchema
