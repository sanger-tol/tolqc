# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcAccession
from main.schema import AccessionSchema

from .base import BaseService, setup_service


@setup_service
class AccessionService(BaseService):
    class Meta:
        model = TolqcAccession
        schema = AccessionSchema
