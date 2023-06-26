# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import DatasetElementService
from main.swagger import DatasetElementSwagger

from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_dataset_element = DatasetElementSwagger.api


@setup_resource_group
class DatasetElementResourceGroup(AutoResourceGroup):
    class Meta:
        service = DatasetElementService
        swagger = DatasetElementSwagger
