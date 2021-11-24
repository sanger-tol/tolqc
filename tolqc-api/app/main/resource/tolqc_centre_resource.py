# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Namespace

from main.schema import TolqcCentreSchema
from .base import BaseDetailResource, BaseListResource


centre_namespace = Namespace('centre', description='Centre related methods')


class TolqcCentreResource(BaseDetailResource):
    name = 'centre'
    schema = TolqcCentreSchema()


class TolqcCentreListResource(BaseListResource):
    name = 'centres'
    schema = TolqcCentreSchema()
