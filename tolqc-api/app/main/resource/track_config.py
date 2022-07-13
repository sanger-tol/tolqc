# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import TrackConfigService
from main.swagger import TrackConfigSwagger

from .base import AutoResourceGroup, setup_resource_group


api_track_config = TrackConfigSwagger.api


@setup_resource_group
class TrackConfigResourceGroup(AutoResourceGroup):
    class Meta:
        service = TrackConfigService
        swagger = TrackConfigSwagger
