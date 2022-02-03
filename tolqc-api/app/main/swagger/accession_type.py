# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import AccessionTypeSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class AccessionTypeSwagger(BaseSwagger):
    class Meta:
        schema = AccessionTypeSchema
