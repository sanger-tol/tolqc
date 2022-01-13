# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model import TolqcProject
from main.schema import ProjectSchema

from .base import BaseService


class ProjectService(BaseService):
    class Meta:
        model = TolqcProject
        schema = ProjectSchema
