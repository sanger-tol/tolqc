# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db, setup_model


@setup_model
class TolqcUser(Base):
    __tablename__ = "user"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    organisation = db.Column(db.String())
    api_key = db.Column(db.String(), unique=True)
    token = db.Column(db.String(), unique=True)
    role = db.relationship('TolqcRole', lazy=False, back_populates="user")

    def to_dict(cls):
        return {'name': cls.name,
                'email': cls.email,
                'organisation': ("" if cls.organisation is None else cls.organisation),
                'role': cls.role}


def get_user_id_via_api_key(api_key):
    user = db.session.query(TolqcUser).filter(TolqcUser.api_key == api_key).one_or_none()
    return user.id if user is not None else None
