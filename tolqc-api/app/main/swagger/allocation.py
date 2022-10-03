# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import AllocationSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class AllocationSwagger(BaseSwagger):
    class Meta:
        schema = AllocationSchema
