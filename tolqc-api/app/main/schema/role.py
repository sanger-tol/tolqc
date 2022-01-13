# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcRole

from .base import BaseSchema, setup_schema


@setup_schema
class RoleSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcRole
