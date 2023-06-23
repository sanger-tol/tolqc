# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import LogBase, db, setup_model


@setup_model
class AssemblyStatus(LogBase):
    __tablename__ = 'assembly_status'

    class Meta:
        type_ = 'assembly_statuses'
        id_column = 'assembly_status_id'

    assembly_status_id = db.Column(db.Integer(), primary_key=True)
    assembly_id = db.Column(
        db.Integer(), db.ForeignKey('assembly.assembly_id'), nullable=False
    )
    status_type_id = db.Column(
        db.String(),
        db.ForeignKey('assembly_status_type.status_type_id'),
        nullable=False,
    )
    status_time = db.Column(db.DateTime(), nullable=False)

    assembly = db.relationship(
        'Assembly', foreign_keys=[assembly_id], back_populates='status_history'
    )
    status_type = db.relationship('AssemblyStatusType', back_populates='statuses')
