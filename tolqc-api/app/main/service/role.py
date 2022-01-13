# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcRole
from main.schema import RoleSchema

from .base import BaseService


class RoleService(BaseService):
    class Meta:
        model = TolqcRole
        schema = RoleSchema
