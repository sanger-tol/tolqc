# SPDX-FileCopyrightText: 2025 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

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
                        f['file'] = '/'.join((prefix, folder_ulid, file))

            return file_list

        return processor


class LastPathElementBundle(Bundle):
    """Return the last element of the path"""

    def create_row_processor(self, query, getters, _):
        (get_path,) = getters

        def processor(row):
            path = get_path(row)
            return path.split('/')[-1] if path else None

        return processor


class StarPathBundle(Bundle):
    """
    Provided that the first element is not null, return all elements joined as
    a path, with `*` replacing any values which are null.
    """

    def create_row_processor(self, query, getters, _):
        def processor(row):
            elements = tuple(g(row) for g in getters)
            if elements[0] is None:
                return None
            else:
                return '/'.join('*' if x is None else x for x in elements)

        return processor


class ProjectGroupBundle(Bundle):
    """
    Combine the "proj" and "taxon_group" columns if the "proj" column
    contains "{}", else returns the "proj" itself.
    e.g. ("darwin/{}", "birds") becomes "darwin/birds"
    """  # noqa: P102

    def create_row_processor(self, query, getters, _):
        get_proj, get_taxon_group = getters

        def processor(row):
            proj = get_proj(row)
            taxon_group = get_taxon_group(row)
            group = None
            if proj is not None:
                if '{}' in proj and taxon_group is not None:  # noqa: P103
                    group = proj.format(taxon_group)
                else:
                    group = proj
            return group

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
