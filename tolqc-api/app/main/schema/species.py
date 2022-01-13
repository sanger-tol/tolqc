# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcSpecies

from .base import BaseSchema, setup_schema


@setup_schema
class SpeciesSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcSpecies
