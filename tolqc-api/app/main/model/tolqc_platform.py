# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcPlatform(Base):
    __tablename__ = "platforms"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    model = db.Column(db.String(), nullable=False)
    runs = db.relationship("TolqcRun", back_populates="platforms")
