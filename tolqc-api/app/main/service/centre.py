# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.schema.centre import CentreDetailSchema


class CentreService:
    @classmethod
    def get_by_id(self, id):
        CentreDetailSchema().read_by_id(id)

    @classmethod
    def put_by_id(self, id, data):
        CentreDetailSchema().update_by_id(id, data)

    @classmethod
    def delete_by_id(self, id):
        CentreDetailSchema().delete_by_id(id)
