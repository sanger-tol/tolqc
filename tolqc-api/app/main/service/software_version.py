# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcSoftwareVersion
from main.schema import SoftwareVersionSchema

from .base import BaseService, setup_service


@setup_service
class SoftwareVersionService(BaseService):
    class Meta:
        model = TolqcSoftwareVersion
        schema = SoftwareVersionSchema
