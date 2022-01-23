# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcBusco
from main.schema import BuscoSchema

from .base import BaseService


class BuscoService(BaseService):
    class Meta:
        model = TolqcBusco
        schema = BuscoSchema
