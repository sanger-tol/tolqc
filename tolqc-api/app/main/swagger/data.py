# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import DataSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class DataSwagger(BaseSwagger):
    class Meta:
        schema = DataSchema
