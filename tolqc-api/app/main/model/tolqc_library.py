# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import Base, db, LogMixin, setup_model


@setup_model
class TolqcLibrary(LogMixin, Base):
    __tablename__ = "library"

    class Meta:
        type_ = 'libraries'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    hierarchy_name = db.Column(db.String())
    library_type_id = db.Column(db.Integer(), db.ForeignKey("library_type.id"))
    lims_id = db.Column(db.Integer())
    data = db.relationship("TolqcData", back_populates="library")
    library_type = db.relationship("TolqcLibraryType", back_populates="library",
                                   foreign_keys=[library_type_id])
