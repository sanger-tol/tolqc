# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import LogBase, db, setup_model


@setup_model
class Status(LogBase):
    __tablename__ = 'status'

    class Meta:
        type_ = 'statuses'

    id = db.Column(db.Integer(), primary_key=True)  # noqa A003
    specimen_id = db.Column(db.Integer(), db.ForeignKey('specimen.id'))
    coverage = db.Column(db.String())
    lims_id = db.Column(db.String())
    note_id = db.Column(db.String())
    status_dict_id = db.Column(db.Integer(), db.ForeignKey('status_dict.id'))
    qc_dict_id = db.Column(db.Integer(), db.ForeignKey('qc_dict.id'))
    milestone_dict_id = db.Column(db.Integer(), db.ForeignKey('milestone_dict.id'))
    specimen = db.relationship('Specimen', back_populates='status')
    status_dict = db.relationship('StatusDict', back_populates='status',
                                  foreign_keys=[status_dict_id])
    qc_dict = db.relationship('QcDict', back_populates='status',
                              foreign_keys=[qc_dict_id])
    milestone_dict = db.relationship('MilestoneDict', back_populates='status',
                                     foreign_keys=[milestone_dict_id])
