# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model.base import Base, db, ExtColumn, setup_model


@setup_model
class A_ModelRelationship(Base):
    __tablename__ = 'A'
    # the variable below is necessary on every test model!
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    B = db.relationship('B_ModelRelationship', back_populates='A')


@setup_model
class B_ModelRelationship(Base):
    __tablename__ = 'B'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    a_id = db.Column(db.Integer, db.ForeignKey("A.id"), nullable=False)
    A = db.relationship(A_ModelRelationship, back_populates='B', foreign_keys=[a_id])
    E = db.relationship('E_ModelRelationship', back_populates='B')


@setup_model
class C_ModelWithNullableColumn(Base):
    __tablename__ = 'C'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    nullable_column = db.Column(db.String, nullable=True)
    other_column = db.Column(db.String, nullable=True)


@setup_model
class D_ModelWithNonNullableColumn(Base):
    __tablename__ = 'D'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    non_nullable_column = db.Column(db.String, nullable=False)
    other_column = db.Column(db.String, nullable=True)


@setup_model
class E_ModelRelationship(Base):
    __tablename__ = 'E'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    b_id = db.Column(db.Integer, db.ForeignKey("B.id"), nullable=False)
    B = db.relationship(B_ModelRelationship, back_populates='E', foreign_keys=[b_id])


@setup_model
class F_ModelWithExtField(Base):
    __tablename__ = 'F'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    ext = ExtColumn()
    other_column = db.Column(db.String, nullable=True)


@setup_model
class G_ModelWithFilterableFields(Base):
    __tablename__ = 'G'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    float_column = db.Column(db.Float, nullable=True)
    bool_column = db.Column(db.Boolean, nullable=True)
    datetime_column = db.Column(db.DateTime, nullable=True)
    string_column = db.Column(db.String, nullable=True)
