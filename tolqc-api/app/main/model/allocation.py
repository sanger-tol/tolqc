# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class Allocation(Base):
    __tablename__ = 'allocation'

    class Meta:
        type_ = 'allocations'

    id = db.Column(db.Integer(), primary_key=True)  # noqa: A003
    project_id = db.Column(db.Integer(), db.ForeignKey('project.project_id'))
    data_id = db.Column(db.Integer(), db.ForeignKey('data.data_id'))
    is_primary = db.Column(db.Boolean())

    db.UniqueConstraint('project_id', 'data_id')

    project = db.relationship('Project', back_populates='data_assn')
    data = db.relationship('Data', back_populates='project_assn')
