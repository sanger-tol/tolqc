# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcUser
from main.schema import UserSchema

from .base import BaseService, setup_service


@setup_service
class UserService(BaseService):
    class Meta:
        model = TolqcUser
        schema = UserSchema
