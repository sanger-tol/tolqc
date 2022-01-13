# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcSpecimen
from main.schema import SpecimenSchema

from .base import BaseService


class SpecimenService(BaseService):
    class Meta:
        model = TolqcSpecimen
        schema = SpecimenSchema
