# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcUser(Base):
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

    @classmethod
    def get_user_infos_by_token(cls, token):
        user_id = cls.query.with_entities(cls.id) \
            .filter(cls.token == token).first()
        return user_id
