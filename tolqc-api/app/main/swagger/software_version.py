# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import SoftwareVersionSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class SoftwareVersionSwagger(BaseSwagger):
    class Meta:
        schema = SoftwareVersionSchema
