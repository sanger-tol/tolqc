# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcSex
from main.schema import SexSchema

from .base import BaseService


class SexService(BaseService):
    class Meta:
        model = TolqcSex
        schema = SexSchema
