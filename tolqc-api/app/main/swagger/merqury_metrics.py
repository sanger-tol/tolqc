# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.schema import MerquryMetricsSchema
from tol.api_base.swagger import BaseSwagger, setup_swagger


@setup_swagger
class MerquryMetricsSwagger(BaseSwagger):
    class Meta:
        schema = MerquryMetricsSchema
