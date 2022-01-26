# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import SeqDataService
from main.swagger import SeqDataSwagger

from .base import BaseResource, setup_resource


api_seq_data = SeqDataSwagger.api


@setup_resource
class SeqDataResource(BaseResource):
    class Meta:
        service = SeqDataService
        swagger = SeqDataSwagger
