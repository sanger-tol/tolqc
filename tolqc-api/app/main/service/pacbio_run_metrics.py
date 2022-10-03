# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcPacbioRunMetrics
from main.schema import PacbioRunMetricsSchema

from .base import BaseService, setup_service


@setup_service
class PacbioRunMetricsService(BaseService):
    class Meta:
        model = TolqcPacbioRunMetrics
        schema = PacbioRunMetricsSchema
