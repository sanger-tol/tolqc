# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import Base, db
from .base import setup_model


@setup_model
class TolqcTrackConfig(Base):
    __tablename__ = "track_config"

    class Meta:
        type_ = 'track_configs'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    lims_id = db.Column(db.Integer())
