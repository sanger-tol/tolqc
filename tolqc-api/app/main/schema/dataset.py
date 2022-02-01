# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcDataset

from .base import BaseSchema, setup_schema


@setup_schema
class DatasetSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcDataset
