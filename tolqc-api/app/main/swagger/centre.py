# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import CentreSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class CentreSwagger(BaseSwagger):
    class Meta:
        schema = CentreSchema
