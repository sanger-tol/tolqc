# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import GenomescopeMetricsSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class GenomescopeMetricsSwagger(BaseSwagger):
    class Meta:
        schema = GenomescopeMetricsSchema
