# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import AssemblyMetricsSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class AssemblyMetricsSwagger(BaseSwagger):
    class Meta:
        schema = AssemblyMetricsSchema
