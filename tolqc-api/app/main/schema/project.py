# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcProject

from .base import BaseSchema, setup_schema


@setup_schema
class ProjectSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcProject
