# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import PacbioRunMetricsSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class PacbioRunMetricsSwagger(BaseSwagger):
    class Meta:
        schema = PacbioRunMetricsSchema
