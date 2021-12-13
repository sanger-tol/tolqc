# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import json

from flask import Response


class BaseService:
    @classmethod
    def _split_error_components(cls, errors):
        titles = [e.get('title', None) for e in errors]
        codes = [e.get('code', None) for e in errors]
        details = [e.get('detail', None) for e in errors]
    
        return titles, codes, details
    
    @classmethod
    def _format_error(cls, title, code, detail):
        return {
            "title": title if title else "Internal Server Error",
            "code": code if code else 500,
            "detail": detail if detail else "An unknown error occured"
        }

    @classmethod
    def custom_post_partial_error(cls, errors=[]):
        titles, codes, details = cls._split_error_components(errors)

        error_messages = [
            None 
            if t is None and c is None and d is None
            else cls._format_error(t, c, d)
            for (t, c, d) in zip(titles, codes, details)
        ]

        return {
            'errors': error_messages
        }

    @classmethod
    def custom_error(cls, status_code=500, errors=[]):
        """Expects a list of dicts, with keys 'title', 'code', and 'detail"""

        titles, codes, details = cls._split_error_components(errors)
        error_messages = [
            cls._format_error(t, c, d)
            for (t, c, d) in zip(titles, codes, details)
        ]

        response = {
            'errors': error_messages
        }

        return Response(
            mimetype="application/json",
            response=json.dumps(response),
            status=status_code
        )
