# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from abc import ABC, abstractmethod

from flask_sqlalchemy import SQLAlchemy
from flask_restx import fields as flask_fields

db = SQLAlchemy()


def populate_once(populate_columns):
    def wrapper(cls, *args, **kwargs):
        # check if already populated
        if cls.populated:
            return
        # indicate that population has occured
        cls.populated = True
        # populate the model's columns
        return populate_columns(cls, *args, **kwargs)
    return wrapper


class Base(ABC, db.Model):
    __abstract__ = True
    schema = {}
    populated = False

    @classmethod
    def _column_to_flask_field(self, column):
        column_type = type(column)

        if column_type == db.Integer:
            return flask_fields.Integer
        if column_type == db.String:
            return flask_fields.String
    
    @classmethod
    def get_api_schema(cls):
        return cls.schema
    
    @classmethod
    def add_column(cls, column_name, *args, in_schema=True, **kwargs):
        locals()[column_name] = db.Column(*args, **kwargs)

        if in_schema == True:
            cls.schema[column_name] = cls._column_to_flask_field(args[0])

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

