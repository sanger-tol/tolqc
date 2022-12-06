# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import Base, db, setup_model


@setup_model
class TolqcPlatform(Base):
    __tablename__ = 'platform'

    class Meta:
        type_ = 'platforms'

    id = db.Column(db.Integer(), primary_key=True)  # noqa A003
    name = db.Column(db.String())
    model = db.Column(db.String())
    run = db.relationship('TolqcRun', back_populates='platform')
