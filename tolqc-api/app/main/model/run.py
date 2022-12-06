# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import LogBase, db, setup_model


@setup_model
class TolqcRun(LogBase):
    __tablename__ = 'run'

    class Meta:
        type_ = 'runs'

    id = db.Column(db.Integer(), primary_key=True)  # noqa A003
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    platform_id = db.Column(db.Integer(), db.ForeignKey('platform.id'))
    centre_id = db.Column(db.Integer(), db.ForeignKey('centre.id'))
    lims_id = db.Column(db.Integer())
    element = db.Column(db.String())
    instrument_name = db.Column(db.String())
    data = db.relationship('TolqcData', back_populates='run')
    platform = db.relationship('TolqcPlatform', back_populates='run',
                               foreign_keys=[platform_id])
    centre = db.relationship('TolqcCentre', back_populates='run',
                             foreign_keys=[centre_id])
    pacbio_run_metrics = db.relationship('TolqcPacbioRunMetrics', back_populates='run')
