# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcStatus

from .base import BaseSchema, setup_schema


@setup_schema
class StatusSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcStatus
