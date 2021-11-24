# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Namespace

from main.schema import TolqcCentreSchema
from .base import BaseResource


centre_namespace = Namespace('centre', description='Centre related methods')


class TolqcCentreResource(BaseResource):
    name = 'centre'
    schema = TolqcCentreSchema()
