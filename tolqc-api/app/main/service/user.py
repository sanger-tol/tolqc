# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcUser
from main.schema import UserSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class UserService(BaseService):
    class Meta:
        model = TolqcUser
        schema = UserSchema
