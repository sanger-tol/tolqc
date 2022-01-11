# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcRole(Base):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    users = db.relationship("TolqcUser", back_populates="roles",
                            uselist=False, foreign_keys=[user_id])

    def to_dict(cls):
        return {'role': cls.role}
