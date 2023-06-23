# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.schema import GenomescopeMetricsSchema
from tol.api_base.swagger import BaseSwagger, setup_swagger


@setup_swagger
class GenomescopeMetricsSwagger(BaseSwagger):
    class Meta:
        schema = GenomescopeMetricsSchema
