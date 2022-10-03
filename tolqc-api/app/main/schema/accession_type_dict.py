# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcAccessionTypeDict

from .base import BaseSchema, setup_schema


@setup_schema
class AccessionTypeDictSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcAccessionTypeDict
