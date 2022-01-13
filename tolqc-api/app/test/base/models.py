# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model.base import Base, db, ExtColumn


class A_ModelRelationship(Base):
    __tablename__ = 'A'
    # the variable below is necessary on every test model!
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    B = db.relationship('B_ModelRelationship', back_populates='A')


class B_ModelRelationship(Base):
    __tablename__ = 'B'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    a_id = db.Column(db.Integer, db.ForeignKey("A.id"), nullable=False)
    A = db.relationship(A_ModelRelationship, back_populates='B', foreign_keys=[a_id])
    E = db.relationship('E_ModelRelationship', back_populates='B')


class C_ModelWithNullableColumn(Base):
    __tablename__ = 'C'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    nullable_column = db.Column(db.String, nullable=True)
    other_column = db.Column(db.String, nullable=True)


class D_ModelWithNonNullableColumn(Base):
    __tablename__ = 'D'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    non_nullable_column = db.Column(db.String, nullable=False)
    other_column = db.Column(db.String, nullable=True)


class E_ModelRelationship(Base):
    __tablename__ = 'E'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    b_id = db.Column(db.Integer, db.ForeignKey("B.id"), nullable=False)
    B = db.relationship(B_ModelRelationship, back_populates='E', foreign_keys=[b_id])


class F_ModelWithExtField(Base):
    __tablename__ = 'F'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    ext = ExtColumn()
    other_column = db.Column(db.String, nullable=True)
