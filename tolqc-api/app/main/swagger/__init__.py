# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .centre import centre_namespace # noqa
from .environment import environment_namespace # noqa
from .run import run_namespace # noqa

authorizations = {
        'ApiKeyAuth': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    }
