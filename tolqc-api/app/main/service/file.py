# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcFile
from main.schema import FileSchema

from .base import BaseService, setup_service


@setup_service
class FileService(BaseService):
    class Meta:
        model = TolqcFile
        schema = FileSchema
