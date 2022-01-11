# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import RunSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class RunSwagger(BaseSwagger):
    class Meta:
        schema = RunSchema
