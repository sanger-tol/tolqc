# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import PlatformSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class PlatformSwagger(BaseSwagger):
    class Meta:
        schema = PlatformSchema
