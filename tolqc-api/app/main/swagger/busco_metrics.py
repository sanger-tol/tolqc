# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import BuscoMetricsSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class BuscoMetricsSwagger(BaseSwagger):
    class Meta:
        schema = BuscoMetricsSchema
