# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema import TolqcCentreSchema
from .base import BaseDetailResource, BaseListResource, BaseNamespace


centre_namespace = BaseNamespace('centre', description='Centre related methods')


class TolqcCentreDetailResource(BaseDetailResource):
    namespace = centre_namespace
    allowed_methods = ['get']
    name = 'centre'
    schema = TolqcCentreSchema()


class TolqcCentreListResource(BaseListResource):
    namespace = centre_namespace
    name = 'centres'
    schema = TolqcCentreSchema()


centre_namespace.add_resource(TolqcCentreDetailResource, '/<int:id>')
centre_namespace.add_resource(TolqcCentreListResource, '')
