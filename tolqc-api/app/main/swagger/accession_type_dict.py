# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import AccessionTypeDictSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class AccessionTypeDictSwagger(BaseSwagger):
    class Meta:
        schema = AccessionTypeDictSchema
