# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import FileSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class FileSwagger(BaseSwagger):
    class Meta:
        schema = FileSchema
