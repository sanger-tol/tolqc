# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.ma import ma


# every child's Meta class must have a type_ and id attribute
class BaseSchema(ma.SQLAlchemyAutoSchema):
    def dump(self, *args, **kwargs):
        data = super().dump(*args, **kwargs)
        meta = self.Meta()
        return {
            "data": {
                "type": meta.type_,
                "id": data[meta.id],
                "attributes": data,
            }
        }
