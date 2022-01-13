# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcSpecies
from main.schema import SpeciesSchema

from .base import BaseService


class SpeciesService(BaseService):
    class Meta:
        model = TolqcSpecies
        schema = SpeciesSchema
