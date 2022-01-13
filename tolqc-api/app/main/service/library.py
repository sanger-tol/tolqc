# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcLibrary
from main.schema import LibrarySchema

from .base import BaseService


class LibraryService(BaseService):
    class Meta:
        model = TolqcLibrary
        schema = LibrarySchema
