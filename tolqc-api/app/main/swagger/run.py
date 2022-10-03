# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import RunSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class RunSwagger(BaseSwagger):
    class Meta:
        schema = RunSchema
