# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import LogBase, db, setup_model


@setup_model
class Project(LogBase):
    __tablename__ = 'project'

    class Meta:
        type_ = 'projects'

    id = db.Column(db.Integer(), primary_key=True)  # noqa A003
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    description = db.Column(db.String())
    lims_id = db.Column(db.Integer())
    accession_id = db.Column(db.Integer(), db.ForeignKey('accession.id'))
    allocation = db.relationship('Allocation', back_populates='project')
    accession = db.relationship('Accession', back_populates='project',
                                foreign_keys=[accession_id])
