# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db, setup_model


@setup_model
class TolqcRole(Base):
    __tablename__ = "role"

    class Meta:
        type_ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("TolqcUser", back_populates="role",
                           uselist=False, foreign_keys=[user_id])

    def to_dict(cls):
        return {'role': cls.role}
