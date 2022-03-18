from sqlalchemy.ext.declarative import declared_attr

from .base import db


class ExtFieldsMixin(object):
    @declared_attr
    def ext(cls):
        return db.Column(
            db.JSON,
            nullable=False,
            default={}
        )

    def _update_ext(self, ext_data_changes):
        ext_data = {**self.ext}
        for key, item in ext_data_changes.items():
            if item is None:
                if key in ext_data:
                    del ext_data[key]
            else:
                ext_data[key] = item
        self.ext = ext_data

    def update(self, data, ext=None, **kwargs):
        if ext is not None:
            self._update_ext(ext)
        super(ExtFieldsMixin, self).update(data, **kwargs)

    @classmethod
    def has_ext_column(cls):
        return True
