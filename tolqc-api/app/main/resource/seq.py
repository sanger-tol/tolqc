# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import SeqService
from main.swagger import SeqSwagger

from .base import BaseListResource, BaseDetailResource, setup_resource


api_seq = SeqSwagger.api


class SeqResourceMeta:
    service = SeqService
    swagger = SeqSwagger


@setup_resource
class SeqDetailResource(BaseDetailResource):
    Meta = SeqResourceMeta


@setup_resource
class SeqListResource(BaseListResource):
    Meta = SeqResourceMeta
