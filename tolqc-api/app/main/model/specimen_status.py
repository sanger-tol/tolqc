# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import LogBase, db, setup_model


@setup_model
class SpecimenStatus(LogBase):
    __tablename__ = 'specimen_status'

    class Meta:
        type_ = 'specimen_statuses'
        id_column = 'specimen_status_id'

    specimen_status_id = db.Column(db.Integer(), primary_key=True)
    specimen_id = db.Column(
        db.String(), db.ForeignKey('specimen.specimen_id'), nullable=False
    )
    status_type_id = db.Column(
        db.String(),
        db.ForeignKey('specimen_status_type.status_type_id'),
        nullable=False,
    )
    status_time = db.Column(db.DateTime(), nullable=False)

    specimen = db.relationship(
        'Specimen', foreign_keys=[specimen_id], back_populates='status_history'
    )
    status_type = db.relationship('SpecimenStatusType', back_populates='statuses')
