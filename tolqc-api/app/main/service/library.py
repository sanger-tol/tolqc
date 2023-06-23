# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from main.model import Library
from main.schema import LibrarySchema
from tol.api_base.service import BaseService, setup_service


@setup_service
class LibraryService(BaseService):
    class Meta:
        model = Library
        schema = LibrarySchema
