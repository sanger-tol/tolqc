# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import SpecimenSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class SpecimenSwagger(BaseSwagger):
    class Meta:
        schema = SpecimenSchema
