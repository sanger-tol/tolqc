# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcRole
from main.schema import RoleSchema

from .base import BaseService, setup_service


@setup_service
class RoleService(BaseService):
    class Meta:
        model = TolqcRole
        schema = RoleSchema
