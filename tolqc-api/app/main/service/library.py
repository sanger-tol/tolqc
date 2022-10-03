# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcLibrary
from main.schema import LibrarySchema

from .base import BaseService, setup_service


@setup_service
class LibraryService(BaseService):
    class Meta:
        model = TolqcLibrary
        schema = LibrarySchema
