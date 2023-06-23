# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.schema import DatasetStatusTypeSchema
from tol.api_base.swagger import BaseSwagger, setup_swagger


@setup_swagger
class DatasetStatusTypeSwagger(BaseSwagger):
    class Meta:
        schema = DatasetStatusTypeSchema
