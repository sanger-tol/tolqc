# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import MerquryService
from main.swagger import MerqurySwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_merqury = MerqurySwagger.api


class MerquryResourceMeta:
    service = MerquryService
    swagger = MerqurySwagger


@setup_resource
class MerquryDetailResource(BaseDetailResource):
    Meta = MerquryResourceMeta


@setup_resource
class MerquryListResource(BaseListResource):
    Meta = MerquryResourceMeta
