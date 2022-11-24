# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import QcDictSchema

from tol.api_base.swagger import BaseSwagger, setup_swagger


@setup_swagger
class QcDictSwagger(BaseSwagger):
    class Meta:
        schema = QcDictSchema
