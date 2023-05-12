# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import LogBase, db, setup_model


@setup_model
class Run(LogBase):
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
    date = db.Column(db.DateTime())
    start_date = db.Column(db.DateTime())
    qc_date = db.Column(db.DateTime())
    complete_date = db.Column(db.DateTime())
    data = db.relationship('Data', back_populates='run')
    platform = db.relationship('Platform', back_populates='run',
                               foreign_keys=[platform_id])
    centre = db.relationship('Centre', back_populates='run',
                             foreign_keys=[centre_id])
    pacbio_run_metrics = db.relationship('PacbioRunMetrics', back_populates='run')
