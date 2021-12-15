# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from flask_restx import fields

from main.model import ExtraFieldsNotPermittedException

class ValidationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class BaseSchema():
    @classmethod
    def get_type(cls):
        return cls.Meta.model.__tablename__

    @classmethod
    def _get_dict_schema(cls, exclude_fields=[]):
        return {
            f: cls._get_field_schema_model_type(f)
            for f in cls._get_fields(
                exclude_fields=exclude_fields+['ext']
            )
        }

    @classmethod
    def _individual_attributes_schem_model_dict(cls, exclude_fields=[]):
        dict_schema = cls._get_dict_schema(exclude_fields=exclude_fields)

        required_fields = cls._get_required_fields(exclude_fields=exclude_fields)

        return {
            'required': required_fields,
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
                    exclude_fields=['id']
                )
            }
        }

    def ext_field_should_not_be_specified(self, data):
        if 'ext' in data.keys() and self.Meta.model.has_ext_column():
            return True
        return False

    @classmethod
    def _to_model_dict(cls, exclude_fields=[], ignore_required=None):
        fields = cls._get_fields(
            exclude_fields=exclude_fields+['id', 'ext']
        )
        return {
            f: cls._get_field_model_type(f, ignore_required)
            for f in fields
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
    def _get_field_model_type(cls, field, ignore_required=None):
        model = cls.Meta.model
        python_type = model.get_column_python_type(
            field
        )
        if not ignore_required:
            required = not model.column_is_nullable(field)
        else:
            required = False

        if python_type == int:
            return fields.Integer(required=required)
        if python_type == str:
            return fields.String(required=required)
        if python_type == bool:
            return fields.Boolean(required=required)
        if python_type == datetime:
            return fields.DateTime(required=required)
        if python_type == float:
            return fields.Float(required=required)

        raise NotImplementedError(
            f"Type '{python_type}' has not been implemented yet."
        )

    @classmethod
    def _get_fields(cls, exclude_fields=[]):
        column_names = cls.Meta.model.get_column_names()
        return [
            c for c in column_names
            if c not in exclude_fields
        ]

    @classmethod
    def _get_non_required_fields(cls):
        return cls.Meta.model.get_nullable_column_names()

    @classmethod
    def _get_required_fields(cls, exclude_fields):
        all_fields = cls._get_fields(exclude_fields)
        non_required_fields = cls._get_non_required_fields()
        return [
            f for f in all_fields
            if f not in non_required_fields
            and f not in exclude_fields
        ]

    def _separate_extra_data(self, data):
        request_fields = data.keys()
        base_fields = self._get_fields([])
        base_data = {
            f: data[f]
            for f in request_fields
            if f in base_fields
        }
        ext_data = {
            f: data[f]
            for f in request_fields
            if f not in base_fields
        }
        if ext_data and not self.Meta.model.has_ext_column():
            raise ExtraFieldsNotPermittedException(ext_data)
        return base_data, ext_data

    def _get_validation_error(self, data):
        if 'id' in data.keys():
            return 'An id must not be specified in the body of a request to this endpoint.'
        required_fields = self._get_required_fields(exclude_fields=['id', 'ext'])
        for field in required_fields:
            if field not in data.keys():
                return f"The field '{field}' is required on this endpoint."
        # TODO add type checking
        return None

    @classmethod
    def to_put_request_model_dict(cls):
        """Returns a dict for a Model, excluding
           the specified list of fields, for a PUT
           request"""
        return cls._to_model_dict(ignore_required=True)

    @classmethod
    def to_detail_response_schema_model_dict(cls):
        """Returns a dict for a SchemaModel in JSON:API format"""
        return {
            'required': ['data'],
            'properties': {
                "data": cls._individual_schema_model_dict()
            },
            'type': 'object',
        }

    def update_by_id(self, id, data):
        return
        validation_error = self._get_validation_error(data)
        if validation_error is not None:
            raise ValidationError(validation_error)
        base_data, ext_data = self._separate_extra_data(data)
        if ext_data:
            base_data['ext'] = ext_data
        model_instance = self._find_model_by_id(id)
        model_instance.update(base_data)
        model_instance.commit()
        return self.dump(model_instance)

    def delete_by_id(self, id):
        return
        model_instance = self._find_model_by_id(id)
        model_instance.delete()
        model_instance.commit()

    def read_bulk(self):
        model = self.Meta.model
        return self.dump(model.find_bulk())

    @classmethod
    def to_list_response_schema_model_dict(cls):
        """Returns a dict for a SchemaModel in JSON:API format"""
        return {
            'required': ['data'],
            'properties': {
                "data": {
                    'type': 'array',
                    'items': cls._individual_schema_model_dict()
                },
                'meta': {
                    'type': 'object',
                    'properties': {
                        "errors": {
                            'type': 'array'
                        }
                    }
                }
            },
            'type': 'object',
        }

    @classmethod
    def _error_schema_model_dict(cls):
        return {
            'required': ['error'],
            'type': 'object',
            'properties': {
                'error': {
                    'type': 'string',
                    'default': 'The error message for this failed create.'
                }
            },
        }

    @classmethod
    def to_post_request_schema_model_dict(cls):
        """Returns a dict for a Model, excluding
           the specified list of fields, for a POST
           request"""
        return {
            'type': 'array',
            'items': cls._individual_attributes_schem_model_dict(
                exclude_fields=['id']
            )
        }
