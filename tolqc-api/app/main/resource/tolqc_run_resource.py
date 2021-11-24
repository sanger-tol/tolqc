# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_restx import Resource, Namespace

from main.model import TolqcRun
from main.schema import TolqcRunSchema


run_namespace = Namespace(
    'run',
    description='ToLQC-Run related methods',
)

run_schema = TolqcRunSchema()


class TolqcRunResource(Resource):
    @run_namespace.doc('Gets the run with the specified id')
    def get(self, id):
        run = TolqcRun.find_by_id(id)
        if run is None:
            return {
                "error": f"Run with id '{id}' not found"
            }, 404

        return run_schema.dump(run), 200
