# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .log_base import LogBase, db
from .base import setup_model


@setup_model
class TolqcPacbioRunStats(LogBase):
    __tablename__ = "pacbio_run_stats"
    id = db.Column(db.Integer(), primary_key=True)
    run_instance_id = db.Column(db.Integer(), db.ForeignKey("runs.id"),
                                nullable=False)
    move_time = db.Column(db.Integer())
    pre_extension_time = db.Column(db.String())
    total_bases = db.Column(db.String())
    polymerase_reads = db.Column(db.String())
    polymerase_reads_bases = db.Column(db.String())
    polymerase_reads_mean = db.Column(db.Float())
    polymerase_reads_n50 = db.Column(db.Float())
    subreads_mean = db.Column(db.Float())
    subreads_n50 = db.Column(db.Float())
    insert_mean = db.Column(db.Float())
    insert_n50 = db.Column(db.Float())
    umy = db.Column(db.String())
    p0 = db.Column(db.String())
    p1 = db.Column(db.String())
    p2 = db.Column(db.String())
    ccs_version_id = db.Column(db.Integer())
    ccs_pass = db.Column(db.String())
    ccs_fail = db.Column(db.String())
    demux_version_id = db.Column(db.Integer())
    demux_pass = db.Column(db.String())
    demux_fail = db.Column(db.String())
    runs = db.relationship("TolqcRun", back_populates="pacbio_run_stats",
                           foreign_keys=[run_instance_id])
