# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcUser(Base):
    __tablename__ = "user"
    user_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    organisation = db.Column(db.String(), nullable=True)
    api_key = db.Column(db.String(), nullable=True, unique=True)
    token = db.Column(db.String(), nullable=True, unique=True)
    roles = db.relationship('TolqcRole', lazy=False, back_populates="user")

    def to_dict(cls):
        return {'name': cls.name,
                'email': cls.email,
                'organisation': ("" if cls.organisation is None else cls.organisation),
                'roles': cls.roles}
