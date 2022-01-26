# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcMerqury
from main.schema import MerqurySchema

from .base import BaseService, setup_service


@setup_service
class MerquryService(BaseService):
    class Meta:
        model = TolqcMerqury
        schema = MerqurySchema
