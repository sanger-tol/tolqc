# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcSoftwareVersion
from main.schema import SoftwareVersionSchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class SoftwareVersionService(BaseService):
    class Meta:
        model = TolqcSoftwareVersion
        schema = SoftwareVersionSchema
