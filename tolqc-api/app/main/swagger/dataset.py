# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import DatasetSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class DatasetSwagger(BaseSwagger):
    class Meta:
        schema = DatasetSchema
