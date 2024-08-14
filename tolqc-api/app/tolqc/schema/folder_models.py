# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from sqlalchemy import (
    BigInteger,
    ForeignKey,
    String,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import (
    declared_attr,
    mapped_column,
    relationship,
)

from tolqc.schema.base import Base


def models_list():
    return [Folder, FolderLocation]


class Folder(Base):
    __tablename__ = 'folder'

    @classmethod
    def get_id_column_name(cls):
        return 'folder_ulid'

    folder_ulid = mapped_column(String, primary_key=True)
    folder_location_id = mapped_column(
        String, ForeignKey('folder_location.folder_location_id'), nullable=False
    )
    image_file_list = mapped_column(JSONB)
    other_file_list = mapped_column(JSONB)
    files_total_bytes = mapped_column(BigInteger)

    folder_location = relationship('FolderLocation', back_populates='folders')


class FolderLocation(Base):
    __tablename__ = 'folder_location'

    @classmethod
    def get_id_column_name(cls):
        return 'folder_location_id'

    folder_location_id = mapped_column(String, primary_key=True)
    uri_prefix = mapped_column(String)
    files_template = mapped_column(JSONB)

    folders = relationship('Folder', back_populates='folder_location')


class HasFolder:
    """Mixin for tables to link to Folder"""

    # ULID of Folder row
    folder_ulid = mapped_column(
        String, ForeignKey('folder.folder_ulid'), nullable=True
    )

    @declared_attr
    @classmethod
    def folder(cls):
        back_rel_name = cls.__tablename__ + '_folders'
        return relationship('Folder', backref=back_rel_name)
