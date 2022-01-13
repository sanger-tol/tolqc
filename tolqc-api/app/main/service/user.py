# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcUser
from main.schema import UserSchema

from .base import BaseService


class UserService(BaseService):
    class Meta:
        model = TolqcUser
        schema = UserSchema
