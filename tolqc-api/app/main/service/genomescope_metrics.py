# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import GenomescopeMetrics
from main.schema import GenomescopeMetricsSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class GenomescopeMetricsService(BaseService):
    class Meta:
        model = GenomescopeMetrics
        schema = GenomescopeMetricsSchema
