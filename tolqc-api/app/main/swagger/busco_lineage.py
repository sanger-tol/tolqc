# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import BuscoLineageSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class BuscoLineageSwagger(BaseSwagger):
    class Meta:
        schema = BuscoLineageSchema
