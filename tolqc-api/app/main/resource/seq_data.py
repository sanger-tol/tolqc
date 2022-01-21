# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import SeqDataService
from main.swagger import SeqDataSwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_SeqData = SeqDataSwagger.api


class SeqDataResourceMeta:
    service = SeqDataService
    swagger = SeqDataSwagger


@setup_resource
class SeqDataDetailResource(BaseDetailResource):
    Meta = SeqDataResourceMeta


@setup_resource
class SeqDataListResource(BaseListResource):
    Meta = SeqDataResourceMeta
