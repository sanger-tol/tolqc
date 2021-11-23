# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import fields, Resource, Namespace

from main.model.tolqc_centre import TolqcCentre
from main.schema.tolqc_centre_schema import TolqcCentreSchema


centre_namespace = Namespace('centre', description='Centre related methods')


centre_schema = TolqcCentreSchema()


centre = centre_namespace.model('Centre', {
    'centre_id': fields.Integer(1),
    'name': fields.String("The centre's name"),
    'hierachy_name': fields.String("The hierachy name"),
})


class TolqcCentreResource(Resource):
    @centre_namespace.doc('Get a Centre by its ID')
    def get(self, id):
        _centre = TolqcCentre.find_by_centre_id(id)
        if _centre is None:
            return {
                "error": f"Centre with id '{id}' not found"
            }, 404

        return centre_schema.dump(_centre), 200

    @centre_namespace.expect(centre)
    def post(self, centre):
        pass
