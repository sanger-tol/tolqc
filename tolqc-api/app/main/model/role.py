# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import Base, db, setup_model


@setup_model
class TolqcRole(Base):
    __tablename__ = "role"

    class Meta:
        type_ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="role",
                           uselist=False, foreign_keys=[user_id])
