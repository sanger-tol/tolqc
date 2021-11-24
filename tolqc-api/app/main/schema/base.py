# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import logging

from main.ma import ma


# every child's Meta class must have an id attribute
class IdNotSpecifiedException(Exception):
    def __init__(self, cls):
        self._cls = cls
        logging.error(self._to_str())

    def _to_str(self):
        return "The schema class for model '%s' does not" \
               "have a specified id in nested class Meta" \
            % self._cls.Meta.model.__tablename__


# every child's Meta class must have a type attribute
class TypeNotSpecifiedException(Exception):
    def __init__(self, cls):
        self._cls = cls
        logging.error(self._to_str())

    def _to_str(self):
        return "The schema class for model '%s' does not" \
               "have a specified type_ in nested class Meta" \
            % self._cls.Meta.model.__tablename__


class BaseSchema(ma.SQLAlchemyAutoSchema):
    @classmethod
    def _get_type(cls):
        type_ = cls.Meta.__dict__.get('type_')
        if type_ is None:
            raise TypeNotSpecifiedException(cls)
        return type_

    @classmethod
    def _get_id(cls):
        id = cls.Meta.__dict__.get('id')
        if id is None:
            raise IdNotSpecifiedException(cls)
        return id

    def dump(self, *args, **kwargs):
        data = super().dump(*args, **kwargs)
        return {
            "data": {
                "type": self._get_type(),
                "id": data[self._get_id()],
                "attributes": data,
            }
        }
