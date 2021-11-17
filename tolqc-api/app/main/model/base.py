# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True

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
