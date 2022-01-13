# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import SpeciesSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class SpeciesSwagger(BaseSwagger):
    class Meta:
        schema = SpeciesSchema
