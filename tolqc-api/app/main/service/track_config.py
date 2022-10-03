# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcTrackConfig
from main.schema import TrackConfigSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class TrackConfigService(BaseService):
    class Meta:
        model = TolqcTrackConfig
        schema = TrackConfigSchema
