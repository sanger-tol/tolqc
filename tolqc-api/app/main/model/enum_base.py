# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class NamedEnumInstanceDoesNotExistException(Exception):
    pass


class EnumBase(Base):
    __abstract__ = True

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), unique=True)
    description = db.Column(db.String(), nullable=True)

    @classmethod
    def is_enum_table(cls):
        return True

    @classmethod
    def get_enum_values(cls):
        query = db.session.query(cls)
        return [m.name for m in query.all()]

    @classmethod
    def find_by_name(cls, name):
        query = db.session.query(cls)
        instance = query.filter_by(name=name).one_or_none()
        if instance is None:
            raise NamedEnumInstanceDoesNotExistException()
        return instance

    @classmethod
    def get_id_from_name(cls, name):
        query = db.session.query(cls)
        instance = query.filter_by(name=name).one_or_none()
        if instance is None:
            return None
        return instance.id

    @classmethod
    def get_name_from_id(cls, id):
        query = db.session.query(cls)
        instance = query.filter_by(id=id).one_or_none()
        if instance is None:
            return None
        return instance.name
