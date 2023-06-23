# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import LibraryType
from main.schema import LibraryTypeSchema
from tol.api_base.service import BaseService, setup_service


@setup_service
class LibraryTypeService(BaseService):
    class Meta:
        model = LibraryType
        schema = LibraryTypeSchema
