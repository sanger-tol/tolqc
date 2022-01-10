# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import UserService
from main.swagger import UserSwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_user = UserSwagger.api


class UserResourceMeta:
    service = UserService
    swagger = UserSwagger


@setup_resource
class UserDetailResource(BaseDetailResource):
    Meta = UserResourceMeta


@setup_resource
class UserListResource(BaseListResource):
    Meta = UserResourceMeta
