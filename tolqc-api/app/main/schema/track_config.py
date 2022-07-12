# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcTrackConfig

from .base import BaseSchema, setup_schema


@setup_schema
class TrackConfigSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcTrackConfig
