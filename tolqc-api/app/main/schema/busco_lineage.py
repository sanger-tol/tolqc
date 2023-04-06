# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import BuscoLineage

from tol.api_base.schema import BaseSchema, setup_schema


@setup_schema
class BuscoLineageSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = BuscoLineage
