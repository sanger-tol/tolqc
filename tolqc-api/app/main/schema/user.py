# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT
from main.model import TolqcUser

from .base import BaseSchema, setup_schema


@setup_schema
class UserSchema(BaseSchema):
    class Meta(BaseSchema.BaseMeta):
        model = TolqcUser
        # exclude access credentials
        exclude = ('api_key', 'token')
