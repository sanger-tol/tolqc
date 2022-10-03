# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcAccession

from .base import BaseSchema, setup_schema


@setup_schema
class AccessionSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcAccession
