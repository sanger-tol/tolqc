# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import SeqService
from main.swagger import SeqSwagger

from .base import BaseResource, setup_resource


api_seq = SeqSwagger.api


@setup_resource
class SeqResource(BaseResource):
    class Meta:
        service = SeqService
        swagger = SeqSwagger
