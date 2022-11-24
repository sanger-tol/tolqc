# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import TrackConfigService
from main.swagger import TrackConfigSwagger

from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_track_config = TrackConfigSwagger.api


@setup_resource_group
class TrackConfigResourceGroup(AutoResourceGroup):
    class Meta:
        service = TrackConfigService
        swagger = TrackConfigSwagger
