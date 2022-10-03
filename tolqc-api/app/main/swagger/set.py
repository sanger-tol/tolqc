# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import SetSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class SetSwagger(BaseSwagger):
    class Meta:
        schema = SetSchema
