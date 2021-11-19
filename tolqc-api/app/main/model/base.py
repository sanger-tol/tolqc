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
        
        # throw not implemented exception
        raise NotImplementedError(
            f"The column type '{column_type}' is not yet implemented."
        )

    @classmethod
    def _get_columns(cls):
        return inspect(cls).mapper.column_attrs
    
    @classmethod
    def get_api_schema(cls):
        columns = cls._get_columns()
        return {c.name : cls._column_to_flask_field(c) for c in columns}
    
    @classmethod
    def _column_to_json_field(self, column):
        column_type = type(column)

        if column_type == db.Integer:
            return int(column)
        if column_type == db.String:
            return str(column)
        
        # throw not implemented exception
        raise NotImplementedError(
            f"The column type '{column_type}' is not yet implemented."
        )

    def to_dict(self):
        columns = self._get_columns()
        return {c.name : self._column_to_json_field(c) for c in columns}

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

