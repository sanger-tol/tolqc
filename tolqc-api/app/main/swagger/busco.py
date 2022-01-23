# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import BuscoSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class BuscoSwagger(BaseSwagger):
    class Meta:
        schema = BuscoSchema
