# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcData
from main.schema import DataSchema

from .base import BaseService, setup_service


@setup_service
class DataService(BaseService):
    class Meta:
        model = TolqcData
        schema = DataSchema
