# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import Data
from main.schema import DataSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class DataService(BaseService):
    class Meta:
        model = Data
        schema = DataSchema
