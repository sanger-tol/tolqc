# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import MerqurySchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class MerqurySwagger(BaseSwagger):
    class Meta:
        schema = MerqurySchema
