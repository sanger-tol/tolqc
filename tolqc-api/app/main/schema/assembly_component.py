# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcAssemblyComponent

from .base import BaseSchema, setup_schema


@setup_schema
class AssemblyComponentSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcAssemblyComponent
