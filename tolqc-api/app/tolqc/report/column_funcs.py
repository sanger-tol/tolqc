# SPDX-FileCopyrightText: 2026 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from typing import Any, TypeAlias

from sqlalchemy import (
    Case,
    ColumnElement,
    Float,
    Function,
    and_,
    case,
    distinct,
    func,
)
from sqlalchemy.orm import InstrumentedAttribute


# SQL column type arguments
ColumnArg: TypeAlias = InstrumentedAttribute[Any] | ColumnElement[Any]  # noqa: UP040


def array_distinct_non_null(label_txt, column):
    """
    Builds SQL for returning an array aggregate column of non-null distinct
    values
    """
    return func.array_remove(func.array_agg(distinct(column)), None).label(label_txt)


def iso_datetime_col(label_txt, column):
    """
    Builds SQL for returning an ISO 8601 datetime string
    """
    return func.to_char(column, 'YYYY-MM-DD"T"HH24:MI:SSTZH:TZM').label(label_txt)


def iso_date_col(label_txt, column):
    """
    Builds SQL for returning an ISO 8601 date string
    """
    return func.to_char(column, 'YYYY-MM-DD').label(label_txt)


def percent_col(label_txt, nominator, divisor, decimal_places=4):
    """
    Builds SQL for returning a column in %
    """
    return (
        func.round(100 * nominator / divisor, decimal_places)
        .cast(Float)
        .label(label_txt)
    )


def star_if_null_path(*path: ColumnArg | str) -> Function[Any]:
    """
    Builds SQL for returning a file path, replacing any null element
    with "*".
    """
    cols = [x if isinstance(x, str) else func.coalesce(x, '*') for x in path]
    return func.concat_ws('/', *cols)


def build_path_if_elements_not_null(*path: ColumnArg) -> Case[Any]:
    """
    Builds SQL for returning a file path when each of the elements in `path`
    is not null.
    """
    all_non_null = tuple(attr.isnot(None) for attr in path)
    return case(
        (
            and_(*all_non_null),
            func.concat_ws('/', *path),
        ),
    )


def build_json_object(*col_list: ColumnArg | tuple[str, ColumnArg]) -> Function[Any]:
    """
    A more compact way to specify JSON object keys and values.
    """
    args = []
    for ele in col_list:
        if isinstance(ele, tuple):
            args.extend(ele)
        else:
            args.append(ele.name)
            args.append(ele)

    return func.json_build_object(*args)
