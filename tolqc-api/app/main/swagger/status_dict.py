# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import StatusDictSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class StatusDictSwagger(BaseSwagger):
    class Meta:
        schema = StatusDictSchema
