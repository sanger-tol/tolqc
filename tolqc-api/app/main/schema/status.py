# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcStatus

from tol.api_base.schema import BaseSchema, setup_schema


@setup_schema
class StatusSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcStatus
