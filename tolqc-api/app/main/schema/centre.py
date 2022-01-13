# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcCentre

from .base import BaseSchema, setup_schema


@setup_schema
class CentreSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcCentre
