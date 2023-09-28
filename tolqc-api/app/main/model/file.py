# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT


from tol.api_base.model import Base, db, setup_model


@setup_model
class File(Base):
    __tablename__ = 'file'

    class Meta:
        type_ = 'files'

    id = db.Column(db.Integer(), primary_key=True)  # noqa: A003
    data_id = db.Column(db.Integer(), db.ForeignKey('data.data_id'))
    name = db.Column(db.String())
    relative_path = db.Column(db.String())
    remote_path = db.Column(db.String())
    size_bytes = db.Column(db.BigInteger())
    md5 = db.Column(db.String())

    data = db.relationship('Data', back_populates='files')
