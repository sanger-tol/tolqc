# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .core_base import CoreBase, db


class TolqcRole(CoreBase):
    __tablename__ = "role"
    role_id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    user = db.relationship("TolqcUser", back_populates="roles",
                           uselist=False, foreign_keys=[user_id])

    def to_dict(cls):
        return {'role': cls.role}
