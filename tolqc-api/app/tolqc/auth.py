# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.auth import require_auth

require_editor = require_auth(role='editor')
