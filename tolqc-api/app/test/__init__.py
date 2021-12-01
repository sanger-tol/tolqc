# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main import application
from flask_testing import TestCase

from main.model import db, Base, TolqcUser, TolqcRole


class ModelRelationshipA(Base):
    __tablename__ = 'test_A'
    id = db.Column(db.Integer, primary_key=True)
    test_B = db.relationship('ModelRelationshipB', back_populates='test_A')


class ModelRelationshipB(Base):
    __tablename__ = 'test_B'
    id = db.Column(db.Integer, primary_key=True)
    a_id = db.Column(db.Integer, db.ForeignKey("test_A.id"), nullable=False)
    test_A = db.relationship(ModelRelationshipA, back_populates='test_B', foreign_keys=[a_id])


class ModelWithNullableColumn(Base):
    __tablename__ = 'test_C'
    id = db.Column(db.Integer, primary_key=True)
    nullable_column = db.Column(db.String, nullable=True)


class ModelWithNonNullableColumn(Base):
    __tablename__ = 'test_D'
    id = db.Column(db.Integer, primary_key=True)
    non_nullable_column = db.Column(db.String, nullable=False)


class BaseTestCase(TestCase):

    api_key = "AnyThingBecAuseThIsIsATEST567890"

    def setUp(self):
        self.maxDiff = None
        db.create_all()
        user1 = TolqcUser(id=100,
                          name="test_user_admin",
                          email="test_user_admin@sanger.ac.uk",
                          organisation="Sanger Institute",
                          api_key=self.api_key)
        db.session.add(user1)
        role = TolqcRole(role="admin")
        role.user = user1
        db.session.add(role)
        db.session.commit()

    def tearDown(self):
        db.session.query(TolqcRole).delete()
        db.session.query(TolqcUser).delete()
        db.session.commit()

    def create_app(self):
        return application()
