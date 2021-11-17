# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main import application

app = application()
reload = True


def main():
    print("Starting ToLQC application...")
    app.run(host='0.0.0.0', debug=True, port=80, use_reloader=reload)


if __name__ == '__main__':
    main()
