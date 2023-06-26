# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.schema import DatasetElementSchema

from tol.api_base.swagger import BaseSwagger, setup_swagger


@setup_swagger
class DatasetElementSwagger(BaseSwagger):
    class Meta:
        schema = DatasetElementSchema
