# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import os

from tol.sql import create_session_factory

from tolqc.flask import application


session_factory = create_session_factory(
    os.environ['DB_URI']
)


app = application(
    session_factory=session_factory
)


def main():
    app.run(
        host='0.0.0.0',
        port=80
    )


if __name__ == '__main__':
    main()
