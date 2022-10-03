# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import MerquryMetricsSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class MerquryMetricsSwagger(BaseSwagger):
    class Meta:
        schema = MerquryMetricsSchema
