# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcBuscoLineage

from .base import BaseSchema, setup_schema


@setup_schema
class BuscoLineageSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcBuscoLineage
