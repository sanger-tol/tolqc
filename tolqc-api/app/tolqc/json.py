# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import datetime
import json

from flask.json.provider import JSONProvider


class JSONDateTimeProvider(JSONProvider):
    """
    Used to replace flask's default encoder. Does not sort keys and formats
    datetime objects using ISO 8601 format instead of flask's default of
    werkzeug.http.http_date
    """

    def dumps(self, obj, **kwargs):
        return json.dumps(obj, separators=(',', ':'), cls=JSONDateTimeEncoder, **kwargs)

    def loads(self, string, **kwargs):
        return json.loads(string, **kwargs)


class JSONDateTimeEncoder(json.JSONEncoder):
    """
    Encode `date` and `datetime` objects in ISO 8601 format.
    """

    def default(self, obj):
        # datetime.datetime is a subclass of date
        if isinstance(obj, datetime.date):
            return obj.isoformat()

        # This line means any exceptions raised will come from the base class
        return json.JSONEncoder.default(self, obj)
