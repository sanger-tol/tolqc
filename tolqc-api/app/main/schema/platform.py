# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcPlatform

from .base import BaseSchema, setup_schema


@setup_schema
class PlatformSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcPlatform
