# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import TrackConfigService
from main.swagger import TrackConfigSwagger

from .base import AutoResourceGroup, setup_resource


api_track_config = TrackConfigSwagger.api


@setup_resource
class TrackConfigResource(AutoResourceGroup):
    class Meta:
        service = TrackConfigService
        swagger = TrackConfigSwagger
