# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.schema import MarkerscanMetricsSchema
from tol.api_base.swagger import BaseSwagger, setup_swagger


@setup_swagger
class MarkerscanMetricsSwagger(BaseSwagger):
    class Meta:
        schema = MarkerscanMetricsSchema
