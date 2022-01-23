# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import AsmStatsSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class AsmStatsSwagger(BaseSwagger):
    class Meta:
        schema = AsmStatsSchema
