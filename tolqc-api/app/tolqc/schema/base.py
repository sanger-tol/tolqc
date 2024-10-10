# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import logging
import os
from datetime import date, datetime
from functools import cache

from caseconverter import pascalcase

import pytz

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    UniqueConstraint,
    event,
    inspect,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import (
    declared_attr,
    mapped_column,
    relationship,
)

from tol.sql import model_base

Base = model_base()


class ModificationBase(Base):
    """
    Classes which contain a `modified_at` and `modified_by` column.
    """

    __abstract__ = True

    @declared_attr
    def modified_at(self):
        """
        Timestamp when row was modified
        """
        return mapped_column(DateTime(timezone=True))

    @declared_attr
    def modified_by(self):
        """
        Who or what modified the row
        """
        return mapped_column(Integer, ForeignKey('user.id'))

    @declared_attr
    def modified_user(self):
        return relationship('User')


class LogBase(ModificationBase):
    __abstract__ = True

    @classmethod
    def edit_table_and_class_names(cls):
        edit_table = 'edit_' + cls.__tablename__
        return edit_table, pascalcase(edit_table)

    @classmethod
    def __declare_first__(cls):
        """Build the EditBase subclass for this LogBase subclass"""
        edit_table_name, edit_class_name = cls.edit_table_and_class_names()
        logging.debug(f"Creating class '{edit_class_name}' for '{cls.__name__}'")
        id_col_name = cls.get_id_column_name()

        # Build specification of new class
        spec = {
            '__tablename__': edit_table_name,
            'edit_id': mapped_column(Integer, primary_key=True),
            # ForeignKey definition causes correct data type (i.e. integer or
            # varchar) to be set.
            id_col_name: mapped_column(
                ForeignKey(f'{cls.__tablename__}.{id_col_name}'), nullable=False
            ),
            # Place `modified_at` first in the unique constraint so that it
            # can be used as an index on `modified_at`, since we already have
            # the foreign key index on `id_col_name`.
            '__table_args__': (UniqueConstraint('modified_at', id_col_name),),
        }

        # Create the edits archive table
        cls.__edit_class = edit_class = type(edit_class_name, (EditBase,), spec)

        # If `back_populates` is set here, then error is thrown:
        #   sqlalchemy.exc.InvalidRequestError:
        #      Mapper 'Mapper[edit_class]' has no property 'edit_of'
        # but `backref` works.
        cls.edit_history = relationship(
            edit_class,
            backref='edit_of',
            order_by=edit_class.modified_at.desc().nullslast(),
        )

    def build_edit_if_changed(self):
        """
        Looks through the state of each column in a potentially updated object. If
        any column has been altered, a new EditBase object is created and
        returned, otherwise `None` is returned.
        """
        state = inspect(self)

        # Loop through `columns` to avoid looking for changes in collections
        # (i.e. one-to-many relationships)
        changes = {}
        for col_name in state.mapper.columns.keys():  # noqa: SIM118
            hist = state.attrs[col_name].history
            if hist.has_changes():
                logging.debug(f'{col_name} changed from {hist.deleted} to {hist.added}')
                cv = hist.deleted[0]
                # Stringify datetime values. `datetime` isa `date`, so we just test for date
                changes[col_name] = cv.isoformat() if isinstance(cv, date) else cv
        if changes:
            # Record the old values, modification time and user in an
            # `EditBase` object
            edit = self.__edit_class(
                edit_of=self,
                changes=changes,
                modified_at=self.modified_at,
                modified_by=self.modified_by,
            )
            return edit
        return None


class EditBase(ModificationBase):
    __abstract__ = True

    @classmethod
    def get_id_column_name(cls):
        return 'edit_id'

    @declared_attr
    def changes(self):
        return mapped_column(JSONB, nullable=False)

    @classmethod
    def __declare_last__(cls):
        """
        Weirdness: without this empty class method not all EditBase mappers
        get configured!
        """


def update_logbase_closure(user_id):
    def update_logbase_before_flush(session, *_):
        """
        Automatically updates log fields in new and changed `LogBase` objects, and
        creates `EditBase` objects to record edit history of changed objects.
        """

        now = now_with_local_tz()

        for new in session.new:
            if not isinstance(new, LogBase):
                continue
            if not inspect(new).pending:
                # Instance has already been saved to database
                continue
            new.modified_at = now
            new.modified_by = user_id

        for upd in session.dirty:
            if not isinstance(upd, LogBase):
                continue
            if not inspect(upd).has_identity:
                # Instance has not yet been saved to database
                continue
            if edit := upd.build_edit_if_changed():
                session.add(edit)
                upd.modified_at = now
                upd.modified_by = user_id

    return update_logbase_before_flush


@event.listens_for(Base, 'mapper_configured', propagate=True)
def log_edit_class(mapper, cls):
    logging.debug(f"Mapper configured for '{cls.__name__}'")


def now_with_local_tz() -> datetime:
    """
    Return the current datetime with the local timezone
    """
    return datetime.now(tz=local_tz())


@cache
def local_tz():
    """
    Cache the local timezone
    """
    return pytz.timezone(os.getenv('TZ', 'Europe/London'))
