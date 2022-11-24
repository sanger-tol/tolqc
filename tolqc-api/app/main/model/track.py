# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import Base, db
from tol.api_base.model import setup_model


@setup_model
class TolqcTrackConfig(Base):
    __tablename__ = "track_config"

    class Meta:
        type_ = 'track_configs'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    lims_id = db.Column(db.Integer())
