# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import LibraryTypeSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class LibraryTypeSwagger(BaseSwagger):
    class Meta:
        schema = LibraryTypeSchema
