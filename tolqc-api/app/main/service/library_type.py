# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcLibraryType
from main.schema import LibraryTypeSchema

from .base import BaseService, setup_service


@setup_service
class LibraryTypeService(BaseService):
    class Meta:
        model = TolqcLibraryType
        schema = LibraryTypeSchema
