# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import File
from main.schema import FileSchema
from tol.api_base.service import BaseService, setup_service


@setup_service
class FileService(BaseService):
    class Meta:
        model = File
        schema = FileSchema
