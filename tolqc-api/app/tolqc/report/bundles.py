# SPDX-FileCopyrightText: 2025 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from urllib.parse import quote

from sqlalchemy.orm import Bundle


class FolderBundle(Bundle):
    """Expand the `file` value of each element of the file list to its complete URL"""

    def create_row_processor(self, query, getters, _):
        get_prefix, get_folder_ulid, get_file_list = getters

        def processor(row):
            prefix = get_prefix(row)
            folder_ulid = get_folder_ulid(row)
            file_list = get_file_list(row)
            if file_list:
                for f in file_list:
                    if file := f.get('file'):
                        f['file'] = '/'.join(
                            (
                                prefix,
                                quote(folder_ulid),
                                quote(file),
                            )
                        )

            return file_list

        return processor


class IsoDayBundle(Bundle):
    """
    Returns just the day portion of a datetime column
    in ISO 8601 format, if it contains a value.
    """

    def create_row_processor(self, query, getters, _):
        (get_datetime,) = getters

        def processor(row):
            dt = get_datetime(row)
            return dt.date().isoformat() if dt else None

        return processor


class IsoDateTimeBundle(Bundle):
    """
    Returns datetime column in ISO 8601 format, if it contains a value.
    """

    def create_row_processor(self, query, getters, _):
        (get_datetime,) = getters

        def processor(row):
            dt = get_datetime(row)
            return dt.isoformat() if dt else None

        return processor
