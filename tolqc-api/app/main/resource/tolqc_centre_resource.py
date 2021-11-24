# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Resource, Namespace

from main.model import TolqcCentre
from main.schema import TolqcCentreSchema


centre_namespace = Namespace('centre', description='Centre related methods')


centre_schema = TolqcCentreSchema()


class TolqcCentreResource(Resource):
    @centre_namespace.doc('Get a Centre by its ID')
    def get(self, id):
        _centre = TolqcCentre.find_by_centre_id(id)
        if _centre is None:
            return {
                "error": f"Centre with id '{id}' not found"
            }, 404

        return centre_schema.dump(_centre), 200
