# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcSpecies
from main.schema import SpeciesSchema

from .base import BaseService, setup_service


@setup_service
class SpeciesService(BaseService):
    class Meta:
        model = TolqcSpecies
        schema = SpeciesSchema
