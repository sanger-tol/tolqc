# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import pytest

from main.model.base import Base, db, setup_model, \
                            ModelValidationError

from test.base import BaseTestCase


class TestModelValidation(BaseTestCase):
    def test_good_model_succeeds(self):
        """A model that declares both __tablename__, and a
        Meta class containing type_"""
        class GoodModel(Base):
            class Meta:
                type_ = 'good'

            __tablename__ = 'TestGG'
            __table_args__ = {'extend_existing': True}

            id = db.Column(db.Integer, primary_key=True)
        
        setup_model(GoodModel)

    def test_model_missing_meta_class_fails(self):
        class BadModel(Base):

            __tablename__ = 'TestBB'
            __table_args__ = {'extend_existing': True}

            id = db.Column(db.Integer, primary_key=True)
        
        with pytest.raises(ModelValidationError):
            setup_model(BadModel)

    def test_model_missing_type_fails(self):
        class BadModel(Base):
            class Meta:
                pass

            __tablename__ = 'TestBB'
            __table_args__ = {'extend_existing': True}

            id = db.Column(db.Integer, primary_key=True)
        
        with pytest.raises(ModelValidationError):
            setup_model(BadModel)