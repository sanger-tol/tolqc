# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.schema import FileSchema
from tol.api_base.swagger import BaseSwagger, setup_swagger


@setup_swagger
class FileSwagger(BaseSwagger):
    class Meta:
        schema = FileSchema
