# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from marshmallow.decorators import post_dump, pre_dump, post_load, pre_load
from marshmallow_jsonapi import Schema as JsonapiSchema, \
                                SchemaOpts as JsonapiSchemaOpts
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, \
                                   SQLAlchemyAutoSchemaOpts
from marshmallow_jsonapi.fields import ResourceMeta, Integer

from main.model import db


def setup_schema(cls):
    cls.setup()
    return cls


class CombinedOpts(JsonapiSchemaOpts, SQLAlchemyAutoSchemaOpts):
    pass


class BaseSchema(SQLAlchemyAutoSchema, JsonapiSchema):
    class BaseMeta(SQLAlchemyAutoSchema.Meta):
        strict = True
        include_resource_linkage = True
        sqla_session = db.session
        load_instance = True

        @classmethod
        def add_views(cls):
            cls.self_view = cls.type_
            cls.self_view_kwargs = {cls.type_: "<id>"}
            cls.self_view_many = cls.type_

    OPTIONS_CLASS = CombinedOpts

    created_by = Integer(dump_only=True)
    resource_meta = ResourceMeta(required=False)

    def __init__(self, **kwargs):
        only = self.get_non_excluded_columns()
        return super().__init__(only=only, **kwargs)

    @classmethod
    def setup(cls):
        cls.Meta.add_views()

    @classmethod
    def get_type(cls):
        return cls.Meta.type_
    
    @classmethod
    def get_non_excluded_columns(cls):
        exclude_columns = ('ext', 'created_by', 'created_at') \
                          if not cls.has_creation_details() \
                          else ('ext',)
        return [
            f for f in cls.get_model_fields()
            if f not in exclude_columns
        ]
    
    @classmethod
    def has_creation_details(cls):
        return cls.Meta.model.has_creation_details()
    
    @classmethod
    def has_ext_field(cls):
        return cls.Meta.model.has_ext_column()

    @classmethod
    def _get_dict_schema(cls, exclude_fields=[]):
        return {
            f: cls._get_field_schema_model_type(f)
            for f in cls.get_model_fields(
                exclude_fields=exclude_fields + ['ext', 'created_by', 'created_at']
            )
        }

    @classmethod
    def _post_attributes_schema_model_dict(cls, exclude_fields=[]):
        dict_schema = cls._get_dict_schema(exclude_fields=exclude_fields)

        required_fields = cls._get_required_fields(exclude_fields=exclude_fields)

        return {
            'required': required_fields,
            'properties': dict_schema,
            'type': 'object',
        }

    @classmethod
    def _patch_attributes_schema_model_dict(cls, exclude_fields=[]):
        dict_schema = cls._get_dict_schema(exclude_fields=exclude_fields)

        return {
            'properties': dict_schema,
            'type': 'object',
        }

    @classmethod
    def _individual_schema_model_dict(cls):
        id_field = cls._get_dict_schema().pop('id', None)

        return {
            'type': 'object',
            'required': ['type', 'attributes', 'id'],
            'properties': {
                "type": {
                    'type': 'string',
                    'default': cls.get_type(),
                },
                "id": id_field,
                "attributes": cls._individual_attributes_schem_model_dict(
                    exclude_fields=['id', 'created_by', 'created_at']
                )
            }
        }

    @classmethod
    def _get_field_schema_model_type(cls, field):
        model = cls.Meta.model
        python_type = model.get_column_python_type(
            field
        )

        if python_type == int:
            return {
                'type': 'integer'
            }
        if python_type == str:
            return {
                'type': 'string'
            }
        if python_type == bool:
            return {
                'type': 'boolean'
            }
        if python_type == datetime:
            return {
                'type': 'string',
                'format': 'date-time'
            }
        if python_type == float:
            return {
                'type': 'number',
                'format': 'float'
            }

        raise NotImplementedError(
            "Type f'{python_type}' has not been implemented yet."
        )

    @classmethod
    def get_model_fields(cls, exclude_fields=[]):
        column_names = cls.Meta.model.get_column_names()
        return [
            c for c in column_names
            if c not in exclude_fields
        ]

    @classmethod
    def _get_non_required_fields(cls):
        return cls.Meta.model.get_nullable_column_names()

    @classmethod
    def _get_required_fields(cls, exclude_fields=[]):
        all_fields = cls.get_model_fields(exclude_fields)
        non_required_fields = cls._get_non_required_fields()
        return [
            f for f in all_fields
            if f not in non_required_fields
            and f not in exclude_fields
        ]

    @classmethod
    def _to_request_schema_model_dict(cls, attributes):
        schema_model_dict = {
            'type': 'object',
            'required': ['data'],
            'properties': {
                "data": {
                    "type": "object",
                    'required': ['type', 'attributes'],
                    'properties': {
                        'type': {
                            'type': 'string',
                            'default': cls.get_type()
                        },
                        'attributes': attributes
                    }
                }
            }
        }
        if not cls.has_ext_field():
            return schema_model_dict
        # add resource level meta
        schema_model_dict['properties']['data']['properties']['meta'] = {
            'type': 'object',
            'properties': {
                'ext': {
                    'type': 'object'
                }
            }
        }
        return schema_model_dict

    @classmethod
    def to_post_request_schema_model_dict(cls):
        """Returns a dict for a Model for a POST request"""
        attributes = cls._post_attributes_schema_model_dict(
            exclude_fields=['id']
        )
        return cls._to_request_schema_model_dict(attributes)

    @classmethod
    def to_patch_request_schema_model_dict(cls):
        """Returns a dict for a Model for a PATCH request"""
        attributes = cls._patch_attributes_schema_model_dict(
            exclude_fields=['id']
        )
        return cls._to_request_schema_model_dict(attributes)
    
    def _make_instance_without_ext(self, data, **kwargs):
        instance = self.instance
        if instance is None:
            return self.Meta.model(**data)
        for field, value in data.items():
            setattr(instance, field, value)
        return instance
    
    def _remove_null_ext_entries_on_create(self, ext):
        return {
            key: value for key, value in ext.items()
            if value is not None
        }
    
    def _make_instance_including_ext(self, data, **kwargs):
        instance = self.instance
        ext = self._none_coalesce_ext(self._resource_meta.pop('ext', {}))
        if instance is None:
            return self.Meta.model(
                **data,
                ext=self._remove_null_ext_entries_on_create(ext)
            )
        for field, value in data.items():
            setattr(instance, field, value)
            instance.update_ext(ext)
        return instance
    
    @pre_load(pass_many=True)
    def test(self, data, many, **kwargs):
        import logging#reeemove
        logging.warning(data)
        # pull out the resource-level metadata. This is likely
        # necessary due to a bug in Marshmallow-Jsonapi
        self._resource_meta = data['data'].pop('meta', {})
        #this shouldn't be necessary >:(
        #if '_resource_meta' in data:
        #    data['resource_meta'] = data.pop('_resource_meta')
        logging.warning(data)
        return data

    @post_load
    def make_instance(self, data, **kwargs):
        # self.instance is part of a private API
        if self.has_ext_field():
            return self._make_instance_including_ext(data, **kwargs)
        return self._make_instance_without_ext(data, **kwargs)
        

    def _none_coalesce_ext(self, ext):
        return ext if ext is not None else {}
    
    def _store_ext_data(self, data, many):
        if many:
            self._ext_data = [
                m.ext for m in data
            ]
        else:
            self._ext_data = data.ext

    @pre_dump(pass_many=True)
    def pre_process_dump_data(self, data, many, **kwargs):
        self._store_ext_data(data, many)

        if many:
            return [
                self._model_instance_to_datum(m)
                for m in data
            ]
        
        return self._model_instance_to_datum(data)

    def _model_instance_to_datum(self, model_instance):
        data = {
            f: getattr(model_instance, f)
            for f in model_instance.get_column_names()
            if f != 'ext'
        }
        if not self.has_ext_field():
            return data

        return data
    
    def _re_insert_ext_datum(self, datum, ext_data):
        datum['meta'] = {
            'ext': ext_data
        }
        return datum
    
    @post_dump(pass_many=True)
    def re_insert_ext_data(self, data, many, **kwargs):
        if many:
            data['data'] = [
                self._re_insert_ext_datum(datum, ext)
                for datum, ext
                in zip(data['data'], self._ext_data)
            ]
        else:
            data['data'] = self._re_insert_ext_datum(
                data['data'],
                self._ext_data
            )
        import logging#reeemove
        logging.warning(data)
        return data
