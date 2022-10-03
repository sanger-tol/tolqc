# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import SampleSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class SampleSwagger(BaseSwagger):
    class Meta:
        schema = SampleSchema
