# SPDX-FileCopyrightText: 2025 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tolqc.reports import RequestArgs


def test_parse_request_args():
    long_string = "X" * 1000
    ra = {
        'true_arg': 'TRUE',
        'false_arg': 'false',
        'null_arg': 'Null',
        'string_arg': 'Vuples vulpes',
        'long_arg': long_string,
    }
    pa = RequestArgs.parse_args(ra)
    assert pa == {
        'true_arg': True,
        'false_arg': False,
        'null_arg': None,
        'string_arg': 'Vuples vulpes',
        'long_arg': long_string[:256]
    }
