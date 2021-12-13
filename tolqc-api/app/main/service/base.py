# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import json

from flask import Response


class BaseService:
    @classmethod
    def custom_error(cls, status_code=500, errors=[]):
        """Expects a list of dicts, with keys 'title', 'code', and 'detail"""

        error_titles = [e.get('title', None) for e in errors]
        error_codes = [e.get('code', None) for e in errors]
        error_details = [e.get('detail', None) for e in errors]

        error_messages = [{
            "title": t if t else "Internal Server Error",
            "code": c if c else 500,
            "detail": d if d else "An unknown error occured"
        } for (t, c, d) in zip(error_titles, error_codes, error_details)]

        response = {
            'errors': error_messages
        }

        return Response(
            mimetype="application/json",
            response=json.dumps(response),
            status=status_code
        )
