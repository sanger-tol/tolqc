# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from connexion.apps.flask_app import FlaskJSONEncoder
from main.model import Base


class JSONEncoder(FlaskJSONEncoder):
    include_nulls = False

    def default(self, o):
        if isinstance(o, Base):
            return o.to_dict()
        return FlaskJSONEncoder.default(self, o)
