# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class DatasetElement(Base):
    __tablename__ = 'dataset_element'

    class Meta:
        type_ = 'dataset_elements'

    id = db.Column(db.Integer(), primary_key=True)  # noqa: A003
    data_id = db.Column(db.Integer(), db.ForeignKey('data.data_id'))
    dataset_id = db.Column(db.String(), db.ForeignKey('dataset.dataset_id'))

    db.UniqueConstraint('data_id', 'dataset_id')

    data = db.relationship('Data', back_populates='dataset_assn')
    dataset = db.relationship('Dataset', back_populates='data_assn')
