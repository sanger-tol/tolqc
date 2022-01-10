# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .creation_log_base import CreationLogBase, db


class TolqcPlatform(CreationLogBase):
    __tablename__ = "platform"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    model = db.Column(db.String(), nullable=False)
    runs = db.relationship("TolqcRun", back_populates="platform")
