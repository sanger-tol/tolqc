# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from datetime import datetime

from flask.json import JSONEncoder as FlaskJSONEncoder

from main.model import Base


class JSONEncoder(FlaskJSONEncoder):
    include_nulls = False

    def default(self, o):
        if isinstance(o, Base):
            return o.to_dict()
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return FlaskJSONEncoder.default(self, o)
