# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main import application

app = application()


def main():
    app.run(
        host='0.0.0.0',
        port=80
    )


if __name__ == '__main__':
    main()
