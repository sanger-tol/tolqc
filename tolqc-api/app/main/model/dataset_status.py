# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import LogBase, db, setup_model


@setup_model
class DatasetStatus(LogBase):
    __tablename__ = 'dataset_status'

    class Meta:
        type_ = 'dataset_statuses'
        id_column = 'dataset_status_id'

    dataset_status_id = db.Column(db.Integer(), primary_key=True)
    dataset_id = db.Column(
        db.String(), db.ForeignKey('dataset.dataset_id'), nullable=False
    )
    status_type_id = db.Column(
        db.String(), db.ForeignKey('dataset_status_type.status_type_id'), nullable=False
    )
    status_time = db.Column(db.DateTime(), nullable=False)

    dataset = db.relationship(
        'Dataset', foreign_keys=[dataset_id], back_populates='status_history'
    )
    status_type = db.relationship('DatasetStatusType', back_populates='statuses')
