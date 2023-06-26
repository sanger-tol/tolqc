# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class Run(Base):
    __tablename__ = 'run'

    class Meta:
        type_ = 'runs'

    id = db.Column(db.Integer(), primary_key=True)  # noqa: A003
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    platform_id = db.Column(db.Integer(), db.ForeignKey('platform.id'))
    centre_id = db.Column(db.Integer(), db.ForeignKey('centre.id'))
    lims_id = db.Column(db.Integer())
    element = db.Column(db.String())
    instrument_name = db.Column(db.String())
    complete = db.Column(db.DateTime())

    data = db.relationship('Data', back_populates='run')
    platform = db.relationship('Platform', back_populates='run')
    centre = db.relationship('Centre', back_populates='run')
    pacbio_run_metrics = db.relationship(
        'PacbioRunMetrics', back_populates='run'
    )
