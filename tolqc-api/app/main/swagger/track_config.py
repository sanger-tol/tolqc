# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import TrackConfigSchema

from .base import BaseSwagger, setup_swagger


@setup_swagger
class TrackConfigSwagger(BaseSwagger):
    class Meta:
        schema = TrackConfigSchema
