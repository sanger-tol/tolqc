# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcAccessionType

from .base import BaseSchema, setup_schema


@setup_schema
class AccessionTypeSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcAccessionType
