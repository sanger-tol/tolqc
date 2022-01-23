# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcBusco

from .base import BaseSchema, setup_schema


@setup_schema
class BuscoSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcBusco
