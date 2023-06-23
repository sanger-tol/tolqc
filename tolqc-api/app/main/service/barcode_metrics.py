# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import BarcodeMetrics
from main.schema import BarcodeMetricsSchema
from tol.api_base.service import BaseService, setup_service


@setup_service
class BarcodeMetricsService(BaseService):
    class Meta:
        model = BarcodeMetrics
        schema = BarcodeMetricsSchema
