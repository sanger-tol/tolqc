# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcSoftwareVersion

from .base import BaseSchema, setup_schema


@setup_schema
class SoftwareVersionSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcSoftwareVersion
