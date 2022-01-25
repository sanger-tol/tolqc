# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcBusco
from main.schema import BuscoSchema

from .base import BaseService, setup_service


@setup_service
class BuscoService(BaseService):
    class Meta:
        model = TolqcBusco
        schema = BuscoSchema
