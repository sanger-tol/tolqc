# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import AccessionSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class AccessionSwagger(BaseSwagger):
    class Meta:
        schema = AccessionSchema
