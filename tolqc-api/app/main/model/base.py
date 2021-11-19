# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_sqlalchemy import SQLAlchemy, inspect
from flask_restx import fields as flask_fields

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True

    @classmethod
    def _column_to_flask_field(self, column):
        column_type = type(column)

        if column_type == db.Integer:
            return flask_fields.Integer
        if column_type == db.String:
            return flask_fields.String
    
    @classmethod
    def get_api_schema(cls):
        columns = inspect(cls).mapper.column_attrs
        schema = {c.name : cls._column_to_flask_field(c) for c in columns}
        
        return schema

    def to_dict(cls):
        return {"override": "this"}

    def add(self):
        db.session.add(self)

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)

    def delete(self):
        db.session.delete(self)

    @classmethod
    def commit(cls):
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def rollback():
        db.session.rollback()

    @staticmethod
    def bulk_update(data):
        db.session.add_all(data)
        db.session.commit()

