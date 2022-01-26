# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import MerquryService
from main.swagger import MerqurySwagger

from .base import BaseResource, setup_resource


api_merqury = MerqurySwagger.api


@setup_resource
class MerquryResource(BaseResource):
    class Meta:
        service = MerquryService
        swagger = MerqurySwagger
