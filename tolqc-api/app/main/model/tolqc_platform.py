# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db


class TolqcPlatform(Base):
    __tablename__ = "platform"
    platform_id = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String())
    model = db.Column(db.String())
