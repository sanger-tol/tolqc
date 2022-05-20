# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main import application

app = application()


def main():
    app.run(
        host='0.0.0.0',
        debug=True,
        port=80
    )


if __name__ == '__main__':
    main()
