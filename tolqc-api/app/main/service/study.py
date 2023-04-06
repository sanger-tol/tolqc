# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import Study
from main.schema import StudySchema

from tol.api_base.service import BaseService, setup_service


@setup_service
class StudyService(BaseService):
    class Meta:
        model = Study
        schema = StudySchema
