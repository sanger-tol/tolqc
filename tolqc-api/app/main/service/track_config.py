# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcTrackConfig
from main.schema import TrackConfigSchema

from .base import BaseService, setup_service


@setup_service
class TrackConfigService(BaseService):
    class Meta:
        model = TolqcTrackConfig
        schema = TrackConfigSchema
