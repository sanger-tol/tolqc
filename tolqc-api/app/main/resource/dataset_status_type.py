# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.service import DatasetStatusTypeService
from main.swagger import DatasetStatusTypeSwagger
from tol.api_base.resource import AutoResourceGroup, setup_resource_group


api_dataset_status_type = DatasetStatusTypeSwagger.api


@setup_resource_group
class DatasetStatusTypeResourceGroup(AutoResourceGroup):
    class Meta:
        service = DatasetStatusTypeService
        swagger = DatasetStatusTypeSwagger
