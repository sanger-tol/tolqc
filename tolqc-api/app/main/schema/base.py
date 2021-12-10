# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from flask_restx import fields
from marshmallow_jsonapi import Schema as JsonapiSchema, \
                                SchemaOpts as JsonapiSchemaOpts
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, \
                                   SQLAlchemyAutoSchemaOpts
from marshmallow_jsonapi.fields import DocumentMeta

from main.model import ExtraFieldsNotPermittedException


class BaseMeta:
    strict = True
    include_fk = True


class RequiredFieldExcludedException(Exception):
    def __init__(self, field, schema):
        super().__init__(
            f"The requied field {field} cannot be excluded"
            f" on schema '{schema.Meta.type_}'."
        )


class InstanceDoesNotExistException(Exception):
    def __init__(self, id, schema):
        super().__init__(
            f"No {schema.Meta.type_} instance"
            f"exists with id {id}."
        )


class ValidationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


def check_excluded_fields_nullable(function):
    def wrapper(schema, *args, exclude_fields=[], **kwargs):
        nullable_fields = schema._get_non_required_fields()
        for field in exclude_fields:
            if field != 'id' and field not in nullable_fields:
                raise RequiredFieldExcludedException(field, schema)
        return function(
            schema,
            *args,
            exclude_fields=exclude_fields,
            **kwargs,
        )
    return wrapper


class BaseSchema():
    @classmethod
    def _get_dict_schema(cls, exclude_fields):
        return {
            f: cls._get_field_schema_model_type(f)
            for f in cls._get_fields(
                exclude_fields=exclude_fields + ['ext']
            )
        }

    @classmethod
    def _individual_attributes_schem_model_dict(cls, exclude_fields):
        dict_schema = cls._get_dict_schema(exclude_fields)

        required_fields = cls._get_required_fields(
            exclude_fields=exclude_fields
        )

        return {
            'required': required_fields,
            'properties': dict_schema,
            'type': 'object',
        }

    @classmethod
    def _individual_schema_model_dict(cls, exclude_fields):
        id_field = cls._get_dict_schema(exclude_fields).pop('id', None)
        if id_field is None:
            raise RequiredFieldExcludedException('id', cls)

        return {
            'type': 'object',
            'required': ['type', 'attributes', 'id'],
            'properties': {
                "type": {
                    'type': 'string',
                    'default': cls.Meta.type_,
                },
                "id": id_field,
                "attributes": cls._individual_attributes_schem_model_dict(
                    exclude_fields=exclude_fields+['id']
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
    def _check_excluded_fields_are_nullable(
        cls,
        nullable_fields,
        exclude_fields
    ):
        for field in nullable_fields:
            # id is not required on request schemas
            if field in exclude_fields and field != "id":
                raise RequiredFieldExcludedException(
                    field, cls
                )

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

# requests are in regular dict format, responses in JSON:API


class CombinedOpts(SQLAlchemyAutoSchemaOpts, JsonapiSchemaOpts):
    pass


class BaseDetailSchema(SQLAlchemyAutoSchema, JsonapiSchema, BaseSchema):
    """Used for individual resources specified by an ID"""

    OPTIONS_CLASS = CombinedOpts

    # TODO move functions out of here, into the correct detail/list inheritor

    @classmethod
    def to_put_request_model_dict(cls, exclude_fields=[]):
        """Returns a dict for a Model, excluding
           the specified list of fields, for a PUT
           request"""
        return cls._to_model_dict(
            exclude_fields=exclude_fields,
            ignore_required=True
        )

    @classmethod
    @check_excluded_fields_nullable
    def to_response_schema_model_dict(cls, exclude_fields=[]):
        """Returns a dict for a SchemaModel in JSON:API format"""
        return {
            'required': ['data'],
            'properties': {
                "data": cls._individual_schema_model_dict(
                    exclude_fields
                )
            },
            'type': 'object',
        }

    def _find_model_by_id(self, id):
        model = self.Meta.model.find_by_id(id)
        if model is None:
            raise InstanceDoesNotExistException(id, self)
        return model

    def read_by_id(self, id):
        model_instance = self._find_model_by_id(id)
        return self.dump(model_instance)

    def update_by_id(self, id, data):
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
        model_instance = self._find_model_by_id(id)
        model_instance.delete()
        model_instance.commit()


class BaseListSchema(SQLAlchemyAutoSchema, JsonapiSchema, BaseSchema):
    """Used for list resources, i.e. operating on multiple
    model instances at a time"""

    OPTIONS_CLASS = CombinedOpts

    document_meta = DocumentMeta()

    # TODO move functions out of here, into the correct detail/list inheritor

    def __init__(self, *args, **kwargs):
        super().__init__(*args, many=True, **kwargs)

    def read_bulk(self):
        model = self.Meta.model
        return self.dump(model.find_bulk())

    def _create_individual(self, datum):
        # TODO error handling
        # TODO use decorators
        validation_error = self._get_validation_error(datum)
        if validation_error is not None:
            return None, validation_error
        if self.ext_field_should_not_be_specified(datum):
            return None, "Do not write directly to the ext field." \
                         " Simply specify the key-value pairs that" \
                         " are not in the schema, and they will be " \
                         "added to the ext field automatically."
        try:
            base_data, ext_data = self._separate_extra_data(datum)
        except ExtraFieldsNotPermittedException:
            return None, "Extra fields are not permitted"

        model = self.Meta.model

        if ext_data:
            kwargs = {'ext': ext_data, **base_data}
        else:
            kwargs = base_data

        model_instance = model(**kwargs)
        error = model_instance.save()
        if error is not None:
            return None, error

        return model_instance, None

    def create_bulk(self, data):
        created = [self._create_individual(d) for d in data]
        instances = [c[0] for c in created]
        errors = [c[1] for c in created]

        if not self.document_meta:
            self.document_meta = self.dict_class()
        self.document_meta.update({"errors": errors})
        return self.dump(instances)

    @classmethod
    @check_excluded_fields_nullable
    def to_response_schema_model_dict(cls, exclude_fields=[]):
        """Returns a dict for a SchemaModel in JSON:API format"""
        return {
            'required': ['data'],
            'properties': {
                "data": {
                    'type': 'array',
                    'items': cls._individual_schema_model_dict(
                        exclude_fields
                    )
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
    @check_excluded_fields_nullable
    def to_post_request_schema_model_dict(cls, exclude_fields=[]):
        """Returns a dict for a Model, excluding
           the specified list of fields, for a POST
           request"""
        non_required_fields = cls._get_non_required_fields()
        for field in exclude_fields:
            if field != 'id' and field not in non_required_fields:
                raise RequiredFieldExcludedException(field, cls)

        return {
            'type': 'array',
            'items': cls._individual_attributes_schem_model_dict(
                exclude_fields=exclude_fields+['id']
            )
        }
