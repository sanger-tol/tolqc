# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.schema import PacbioRunMetricsSchema

from tol.api_base.swagger import BaseSwagger, setup_swagger


@setup_swagger
class PacbioRunMetricsSwagger(BaseSwagger):
    class Meta:
        schema = PacbioRunMetricsSchema
