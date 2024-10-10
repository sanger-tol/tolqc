# SPDX-FileCopyrightText: 2024 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import json

import pytest

from tolqc.marshal.ndjson import (
    cleanup,
    cleanup_string_whitespace,
    must_get_row_value,
    parse_ndjson_row,
    row_message,
)
from tolqc.marshal.seq_data import maybe_datetime


def test_row_message():
    expected = ''.join(
        (
            'Bad row:\n',
            '        n = 10\n',
            '  missing = None\n',
            "  present = 'val'\n",
        )
    )
    assert (
        row_message(
            {
                'n': 10,
                'missing': None,
                'present': 'val',
            },
            'Bad row',
        )
        == expected
    )


def test_must_get():
    assert must_get_row_value({'a': 2}, 'a') == 2
    with pytest.raises(ValueError):
        must_get_row_value({'a': 2}, 'b')


def test_maybe_datetime():
    assert maybe_datetime({}, 'date_x') is None
    dt_str = '1981-09-19T18:30:00-04:00'
    dt = maybe_datetime({'date_x': dt_str}, 'date_x')
    assert dt.isoformat() == dt_str


def test_row_parse():
    too_big = json.dumps({'x': '#' * 100_000})
    with pytest.raises(ValueError):
        parse_ndjson_row(too_big)
    with pytest.raises(ValueError):
        parse_ndjson_row('["ele"]')
    with pytest.raises(ValueError):
        parse_ndjson_row('"x"')
    assert parse_ndjson_row('{"x": "  "}') == {'x': None}


def test_cleanup():
    assert cleanup(' ') is None
    assert cleanup(' x ') == 'x'
    assert cleanup(3.14) == 3.14
    assert cleanup([7, 8, ' ']) == [7, 8, None]
    assert cleanup({' x ': [7, 8, ' ']}) == {'x': [7, 8, None]}
    assert cleanup(
        {
            ' x ': [
                {' a': 1, ' b': 2},
                {'a ': 3, 'b ': ''},
            ],
            'y': 3.14,
        }
    ) == {
        'x': [
            {'a': 1, 'b': 2},
            {'a': 3, 'b': None},
        ],
        'y': 3.14,
    }
    with pytest.raises(ValueError):
        cleanup({7: 'x'})
    with pytest.raises(ValueError):
        cleanup({' ': 'x'})


def test_cleanup_string_whitespace():
    assert cleanup_string_whitespace(' x ') == 'x'
    assert cleanup_string_whitespace(' ') is None
    assert cleanup_string_whitespace('\t\n') is None
