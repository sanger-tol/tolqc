# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from tol.api_base.model import Base, db, setup_model


@setup_model
class Study(Base):
    __tablename__ = 'study'

    class Meta:
        type_ = 'studies'

    id = db.Column(db.Integer(), primary_key=True)  # noqa A003
    name = db.Column(db.String())
    lims_id = db.Column(db.Integer())
    project_id = db.Column(db.Integer(), db.ForeignKey('project.id'))
    project = db.relationship('Project', back_populates='study',
                              foreign_keys=[project_id])
