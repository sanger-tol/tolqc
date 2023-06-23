# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.schema import BuscoMetricsSchema
from tol.api_base.swagger import BaseSwagger, setup_swagger


@setup_swagger
class BuscoMetricsSwagger(BaseSwagger):
    class Meta:
        schema = BuscoMetricsSchema
