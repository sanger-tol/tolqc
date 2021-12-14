# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Namespace

from main.schema import CentreDetailSchema, \
                        CentreListSchema

from .base import BaseSwagger


class CentreSwagger(BaseSwagger):
    detail_schema = CentreDetailSchema
    list_schema = CentreListSchema
    
    api = Namespace(
        'centres',
        description='Centre related methods',
    )


CentreSwagger.populate_default_models()
