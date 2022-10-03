# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import LibraryTypeSchema

from tol.api_base.swagger import BaseSwagger, setup_swagger


@setup_swagger
class LibraryTypeSwagger(BaseSwagger):
    class Meta:
        schema = LibraryTypeSchema
