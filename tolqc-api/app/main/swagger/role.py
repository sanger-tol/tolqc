# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import RoleSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class RoleSwagger(BaseSwagger):
    class Meta:
        schema = RoleSchema
