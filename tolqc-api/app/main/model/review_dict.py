# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class ReviewDict(Base):
    __tablename__ = 'review_dict'

    class Meta:
        type_ = 'review_dicts'
        id_column = 'review_id'

    review_id = db.Column(db.String(), primary_key=True)
    description = db.Column(db.String())

    genomescope_metrics = db.relationship(
        'GenomescopeMetrics', back_populates='review'
    )
