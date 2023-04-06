# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import LogBase, db, setup_model


@setup_model
class Allocation(LogBase):
    __tablename__ = 'allocation'

    class Meta:
        type_ = 'allocations'

    id = db.Column(db.Integer(), primary_key=True)  # noqa A003
    project_id = db.Column(db.Integer(), db.ForeignKey('project.id'))
    specimen_id = db.Column(db.Integer(), db.ForeignKey('specimen.id'))
    is_primary = db.Column(db.Boolean())
    project = db.relationship('Project', back_populates='allocation',
                              foreign_keys=[project_id])
    specimen = db.relationship('Specimen', back_populates='allocation',
                               foreign_keys=[specimen_id])
