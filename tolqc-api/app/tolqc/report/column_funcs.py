# SPDX-FileCopyrightText: 2026 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from sqlalchemy import Float, distinct, func


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


def star_if_null_path(*path):
    """
    Builds SQL for returning a file path, replacing any null null with '*'
    """
    cols = [func.coalesce(x, '*') for x in path]
    return func.concat_ws('/', *cols)
