# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main.model.base import Base, db, setup_model, LogMixin, EnumBase

#TODO FIX THIS!!!
ExtColumn = lambda *args: None


@setup_model
class A_ModelRelationship(Base):
    __tablename__ = 'test_A'

    class Meta:
        type_ = 'A'

    # the variable below is necessary on every test model!
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    test_B = db.relationship('B_ModelRelationship', back_populates='test_A')


@setup_model
class B_ModelRelationship(Base):
    __tablename__ = 'test_B'

    class Meta:
        type_ = 'B'

    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    a_id = db.Column(db.Integer, db.ForeignKey("test_A.id"), nullable=False)
    test_A = db.relationship(A_ModelRelationship, back_populates='test_B', foreign_keys=[a_id])
    test_E = db.relationship('E_ModelRelationship', back_populates='test_B')


@setup_model
class C_ModelWithNullableColumn(Base):
    __tablename__ = 'test_C'

    class Meta:
        type_ = 'C'

    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    nullable_column = db.Column(db.String, nullable=True)
    other_column = db.Column(db.String, nullable=True)


@setup_model
class D_ModelWithNonNullableColumn(Base):
    __tablename__ = 'test_D'

    class Meta:
        type_ = 'D'

    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    non_nullable_column = db.Column(db.String, nullable=False)
    other_column = db.Column(db.String, nullable=True)


@setup_model
class E_ModelRelationship(Base):
    __tablename__ = 'test_E'

    class Meta:
        type_ = 'E'

    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    b_id = db.Column(db.Integer, db.ForeignKey("test_B.id"), nullable=False)
    test_B = db.relationship(B_ModelRelationship, back_populates='test_E', foreign_keys=[b_id])


@setup_model
class F_ModelWithExtField(Base):
    __tablename__ = 'test_F'

    class Meta:
        type_ = 'F'

    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    ext = ExtColumn()
    other_column = db.Column(db.String, nullable=True)


@setup_model
class G_ModelWithFilterableFields(Base):
    __tablename__ = 'test_G'

    class Meta:
        type_ = 'G'

    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    float_column = db.Column(db.Float, nullable=True)
    bool_column = db.Column(db.Boolean, nullable=True)
    datetime_column = db.Column(db.DateTime, nullable=True)
    string_column = db.Column(db.String, nullable=True)


@setup_model
class H_ModelLog(Base, LogMixin):
    __tablename__ = 'test_H'

    class Meta:
        type_ = 'H'

    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    string_column = db.Column(db.String, nullable=True)


@setup_model
class I_ModelEnum(EnumBase):
    __tablename__ = 'test_I'

    class Meta:
        type_ = 'I'

    __table_args__ = {'extend_existing': True}
    test_J = db.relationship('J_ModelEnumDependent', back_populates='test_I')


@setup_model
class J_ModelEnumDependent(Base):
    __tablename__ = 'test_J'

    class Meta:
        type_ = 'J'

    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    i_id = db.Column(db.Integer, db.ForeignKey("test_I.id"), nullable=False)
    test_I = db.relationship(I_ModelEnum, back_populates='test_J', foreign_keys=[i_id])
