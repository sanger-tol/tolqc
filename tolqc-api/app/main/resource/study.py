# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.service import StudyService
from main.swagger import StudySwagger

from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_study = StudySwagger.api


@setup_resource_group
class StudyResourceGroup(AutoResourceGroup):
    class Meta:
        service = StudyService
        swagger = StudySwagger
