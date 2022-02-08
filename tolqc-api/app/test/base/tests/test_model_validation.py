# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import pytest

from main.model.base import Base, db, setup_model

from test.base import BaseTestCase


class TestModelValidation(BaseTestCase):
    def test_good_model_succeeds(self):
        """A model that declares both __tablename__, and a
        Meta class containing type_"""
        class GoodModel(Base):
            class Meta:
                type_ = 'good'

            __tablename__ = 'good name'

            id = db.Column(db.Integer, primary_key=True)
        
        setup_model(GoodModel)