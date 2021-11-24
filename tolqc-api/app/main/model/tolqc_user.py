# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .core_base import CoreBase, db


class TolqcUser(CoreBase):
    __tablename__ = "user"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    organisation = db.Column(db.String())
    api_key = db.Column(db.String(), unique=True)
    token = db.Column(db.String(), unique=True)
    roles = db.relationship('TolqcRole', lazy=False, back_populates="user")

    def to_dict(cls):
        return {'name': cls.name,
                'email': cls.email,
                'organisation': ("" if cls.organisation is None else cls.organisation),
                'roles': cls.roles}
