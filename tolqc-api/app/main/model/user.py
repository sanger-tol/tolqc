# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .tol.api_base.model import Base, db, setup_model


@setup_model
class TolqcUser(Base):
    __tablename__ = "user"

    class Meta:
        type_ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    organisation = db.Column(db.String())
    api_key = db.Column(db.String(), unique=True)
    token = db.Column(db.String(), unique=True)
    role = db.relationship('TolqcRole', lazy=False, back_populates="user")


def get_user_id_via_api_key(api_key):
    user = db.session.query(TolqcUser).filter(TolqcUser.api_key == api_key).one_or_none()
    return user.id if user is not None else None
