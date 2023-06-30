# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.schema import QCDictSchema

from tol.api_base.swagger import BaseSwagger, setup_swagger


@setup_swagger
class QCDictSwagger(BaseSwagger):
    class Meta:
        schema = QCDictSchema
