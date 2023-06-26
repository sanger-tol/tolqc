# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from sqlalchemy.ext.associationproxy import association_proxy

from tol.api_base.model import Base, db, setup_model


@setup_model
class Project(Base):
    __tablename__ = 'project'

    class Meta:
        type_ = 'projects'
        id_column = 'project_id'

    project_id = db.Column(db.Integer(), primary_key=True)
    hierarchy_name = db.Column(db.String())
    description = db.Column(db.String())
    lims_id = db.Column(db.Integer(), index=True)
    accession_id = db.Column(
        db.String(), db.ForeignKey('accession.accession_id')
    )

    accession = db.relationship('Accession', back_populates='projects')
    data_assn = db.relationship('Allocation', back_populates='project')
    data = association_proxy('data_assn', 'data')
