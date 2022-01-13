# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import AllocationService
from main.swagger import AllocationSwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_allocation = AllocationSwagger.api


class AllocationResourceMeta:
    service = AllocationService
    swagger = AllocationSwagger


@setup_resource
class AllocationDetailResource(BaseDetailResource):
    Meta = AllocationResourceMeta


@setup_resource
class AllocationListResource(BaseListResource):
    Meta = AllocationResourceMeta
