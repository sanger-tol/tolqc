# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model.base import Base, db, ExtColumn


class ModelRelationshipA(Base):
    __tablename__ = 'test_A'
    # the variable below is necessary on every test model!
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    test_B = db.relationship('ModelRelationshipB', back_populates='test_A')


class ModelRelationshipB(Base):
    __tablename__ = 'test_B'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    a_id = db.Column(db.Integer, db.ForeignKey("test_A.id"), nullable=False)
    test_A = db.relationship(ModelRelationshipA, back_populates='test_B', foreign_keys=[a_id])
    test_E = db.relationship('ModelRelationshipE', back_populates='test_B')


class ModelWithNullableColumnC(Base):
    __tablename__ = 'test_C'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    nullable_column = db.Column(db.String, nullable=True)
    other_column = db.Column(db.String, nullable=True)


class ModelWithNonNullableColumnD(Base):
    __tablename__ = 'test_D'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    non_nullable_column = db.Column(db.String, nullable=False)
    other_column = db.Column(db.String, nullable=True)


class ModelRelationshipE(Base):
    __tablename__ = 'test_E'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    b_id = db.Column(db.Integer, db.ForeignKey("test_B.id"), nullable=False)
    test_B = db.relationship(ModelRelationshipB, back_populates='test_E', foreign_keys=[b_id])


class ModelWithExtFieldF(Base):
    __tablename__ = 'test_F'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    ext = ExtColumn()
    other_column = db.Column(db.String, nullable=True)
