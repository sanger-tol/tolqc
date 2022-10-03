# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcSpecimen

from .base import BaseSchema, setup_schema


@setup_schema
class SpecimenSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcSpecimen
