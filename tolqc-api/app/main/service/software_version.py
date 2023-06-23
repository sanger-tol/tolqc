# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import SoftwareVersion
from main.schema import SoftwareVersionSchema
from tol.api_base.service import BaseService, setup_service


@setup_service
class SoftwareVersionService(BaseService):
    class Meta:
        model = SoftwareVersion
        schema = SoftwareVersionSchema
