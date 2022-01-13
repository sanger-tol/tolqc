# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import LibrarySchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class LibrarySwagger(BaseSwagger):
    class Meta:
        schema = LibrarySchema
