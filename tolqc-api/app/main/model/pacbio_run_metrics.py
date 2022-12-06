# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import LogBase, db, setup_model


@setup_model
class TolqcPacbioRunMetrics(LogBase):
    __tablename__ = 'pacbio_run_metrics'

    class Meta:
        type_ = 'pacbio_run_metrics'

    id = db.Column(db.Integer(), primary_key=True)  # noqa A003
    run_id = db.Column(db.Integer(), db.ForeignKey('run.id'))
    move_time = db.Column(db.Integer())
    pre_extension_time = db.Column(db.Integer())
    total_bases = db.Column(db.Integer())
    polymerase_reads = db.Column(db.Integer())
    polymerase_reads_bases = db.Column(db.Integer())
    polymerase_reads_mean = db.Column(db.Float())
    polymerase_reads_n50 = db.Column(db.Float())
    subreads_mean = db.Column(db.Float())
    subreads_n50 = db.Column(db.Float())
    insert_mean = db.Column(db.Float())
    insert_n50 = db.Column(db.Float())
    unique_molecular_bases = db.Column(db.Integer())
    p0 = db.Column(db.Integer())
    p1 = db.Column(db.Integer())
    p2 = db.Column(db.Integer())
    ccs_version_id = db.Column(db.String())
    ccs_pass = db.Column(db.Integer())
    ccs_fail = db.Column(db.Integer())
    demux_version_id = db.Column(db.String())
    demux_pass = db.Column(db.Integer())
    demux_fail = db.Column(db.Integer())
    run = db.relationship('TolqcRun', back_populates='pacbio_run_metrics',
                          foreign_keys=[run_id])
