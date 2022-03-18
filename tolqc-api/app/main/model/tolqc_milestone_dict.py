# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from .base import db, EnumBase, setup_model


@setup_model
class TolqcMilestoneDict(EnumBase):
    __tablename__ = "milestone_dict"

    class Meta:
        type_ = 'milestone_types'

    status = db.relationship("TolqcStatus", back_populates="milestone_dict")
