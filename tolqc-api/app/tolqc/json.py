# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import datetime
import json
import os

from flask.json.provider import JSONProvider

import pytz


class JSONDateTimeProvider(JSONProvider):
    """
    Used to replace flask's default encoder. Does not sort keys and formats
    datetime objects using ISO 8601 format instead of flask's default of
    werkzeug.http.http_date
    """

    def dumps(self, obj, **kwargs):
        return json.dumps(
            obj, separators=(',', ':'), cls=JSONDateTimeZoneEncoder, **kwargs
        )

    def loads(self, string, **kwargs):
        return json.loads(string, **kwargs)


DEFAULT_TZ = pytz.timezone(os.getenv('TZ', 'Europe/London'))


class JSONDateTimeZoneEncoder(json.JSONEncoder):
    """
    Encode `date` and `datetime` objects in ISO 8601 format, and add the
    default, local timezone to any "naive" datetime objects before encoding.
    """

    def default(self, obj):
        # Test for datetime first, since it is a subclass of date
        if isinstance(obj, datetime.datetime):
            # Is the datetime timezone "aware"?
            if not obj.tzinfo or obj.tzinfo.utcoffset(obj) is None:
                # No, datetime is "naive"
                obj = DEFAULT_TZ.localize(obj)
            return obj.isoformat()
        if isinstance(obj, datetime.date):
            return obj.isoformat()

        # This line means any exceptions raised will come from the base class
        return json.JSONEncoder.default(self, obj)
