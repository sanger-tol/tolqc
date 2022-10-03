# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcBuscoLineage
from main.schema import BuscoLineageSchema

from .base import BaseService, setup_service


@setup_service
class BuscoLineageService(BaseService):
    class Meta:
        model = TolqcBuscoLineage
        schema = BuscoLineageSchema
