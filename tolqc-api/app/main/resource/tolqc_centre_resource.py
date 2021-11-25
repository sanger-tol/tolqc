# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Namespace

from main.schema import TolqcCentreSchema
from .base import BaseDetailResource, BaseListResource


centre_namespace = Namespace('centre', description='Centre related methods')


class TolqcCentreDetailResource(BaseDetailResource):
    allowed_methods = ['get']
    name = 'centre'
    schema = TolqcCentreSchema()


class TolqcCentreListResource(BaseListResource):
    name = 'centres'
    schema = TolqcCentreSchema()


centre_namespace.add_resource(TolqcCentreDetailResource, '/<int:id>')
centre_namespace.add_resource(TolqcCentreListResource, '')
