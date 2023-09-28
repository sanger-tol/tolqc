# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import json
from datetime import datetime

from main.model import Base


class JSONEncoder(json.JSONEncoder):
    include_nulls = False

    def default(self, o):
        if isinstance(o, Base):
            return o.to_dict()
        if isinstance(o, datetime):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)
