# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcCentre
from main.schema import CentreSchema

from .base import BaseService, setup_service


@setup_service
class CentreService(BaseService):
    class Meta:
        model = TolqcCentre
        schema = CentreSchema
