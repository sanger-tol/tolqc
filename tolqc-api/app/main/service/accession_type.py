# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcAccessionType
from main.schema import AccessionTypeSchema

from .base import BaseService, setup_service


@setup_service
class AccessionTypeService(BaseService):
    class Meta:
        model = TolqcAccessionType
        schema = AccessionTypeSchema
