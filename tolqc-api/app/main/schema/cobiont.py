# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcCobiont

from .base import BaseSchema, setup_schema


@setup_schema
class CobiontSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcCobiont
