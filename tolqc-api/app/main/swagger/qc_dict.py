# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import QcDictSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class QcDictSwagger(BaseSwagger):
    class Meta:
        schema = QcDictSchema
