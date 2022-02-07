# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcAccessionTypeDict

from .base import BaseSchema, setup_schema


@setup_schema
class AccessionTypeDictSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcAccessionTypeDict
