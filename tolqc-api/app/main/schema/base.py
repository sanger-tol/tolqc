# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from flask_restx import fields
from marshmallow import Schema as MarshmallowSchema, \
                        SchemaOpts as MarshmallowSchemaOpts
import marshmallow
from marshmallow.schema import Schema
from marshmallow_jsonapi import Schema as JsonapiSchema, \
                                SchemaOpts as JsonapiSchemaOpts
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, \
                                   SQLAlchemyAutoSchemaOpts
from marshmallow_jsonapi.fields import DocumentMeta, \
                                       BaseRelationship, \
                                       ResourceMeta

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


class IdSpecifiedInRequestBodyException(Exception):
    pass


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
    def _get_fields(cls, exclude_fields):
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

    def _find_model_by_id(self, id):
        model = self.Meta.model.find_by_id(id)
        if model is None:
            raise InstanceDoesNotExistException(id, self)
        return model

    def _separate_extra_data(self, data):
        request_fields = data.keys()
        if 'id' in request_fields:
            raise IdSpecifiedInRequestBodyException()
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

    def create_individual(self, data):
        base_data, ext_data = self._separate_extra_data(data)
        model = self.Meta.model

        if ext_data:
            model_instance = model(ext=ext_data, **base_data)
        else:
            model_instance = model(**base_data)
        model_instance.save()
        return model_instance

    def read_by_id(self, id):
        model_instance = self._find_model_by_id(id)
        return self.dump(model_instance)

    def update_by_id(self, id, data):
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

# requests are in regular dict format, responses in JSON:API


class RequestCombinedOpts(SQLAlchemyAutoSchemaOpts, MarshmallowSchemaOpts):
    pass


class BaseDetailRequestSchema(SQLAlchemyAutoSchema, MarshmallowSchema, BaseSchema):
    """Used for request/input"""

    OPTIONS_CLASS = RequestCombinedOpts

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
    def _to_model_dict(cls, exclude_fields=[], ignore_required=None):
        fields = cls._get_fields(
            exclude_fields=exclude_fields+['id', 'ext']
        )
        return {
            f: cls._get_field_model_type(f, ignore_required)
            for f in fields
        }

    @classmethod
    @check_excluded_fields_nullable
    def to_post_model_dict(cls, exclude_fields=[]):
        """Returns a dict for a Model, excluding
           the specified list of fields, for a POST
           request"""
        non_required_fields = cls._get_non_required_fields()
        for field in exclude_fields:
            if field != 'id' and field not in non_required_fields:
                raise RequiredFieldExcludedException(field, cls)

        return cls._to_model_dict(
            exclude_fields=exclude_fields,
            ignore_required=False
        )

    @classmethod
    def to_put_model_dict(cls, exclude_fields=[]):
        """Returns a dict for a Model, excluding
           the specified list of fields, for a PUT
           request"""
        return cls._to_model_dict(
            exclude_fields=exclude_fields,
            ignore_required=True
        )


class ResponseCombinedOpts(SQLAlchemyAutoSchemaOpts, JsonapiSchemaOpts):
    pass


class BaseDetailResponseSchema(SQLAlchemyAutoSchema, JsonapiSchema, BaseSchema):
    """Used for response/output"""

    OPTIONS_CLASS = ResponseCombinedOpts

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

    # overrides
    def format_item(self, item):
        """Sourced from Marshmallow-jsonapi (MIT License)
        Format a single datum as a Resource object.
        See: http://jsonapi.org/format/#document-resource-objects
        """
        # TODO add license somewhere

        # http://jsonapi.org/format/#document-top-level
        # Primary data MUST be either... a single resource object, a single resource
        # identifier object, or null, for requests that target single resources
        TYPE = "type"
        ID = "id"

        if not item:
            return None

        ret = self.dict_class()
        ret[TYPE] = self.opts.type_

        # Get the schema attributes so we can confirm `dump-to` values exist
        attributes = {
            (self.fields[field].data_key or field): field for field in self.fields
        }

        for field_name, value in item.items():
            # intercept external field
            if field_name == 'ext':
                for ext_field_name, ext_field_value in value.items():
                    if "attributes" not in ret:
                        ret["attributes"] = self.dict_class()
                    ret["attributes"][ext_field_name] = ext_field_value
                continue
            attribute = attributes[field_name]
            if attribute == ID:
                ret[ID] = value
            elif isinstance(self.fields[attribute], DocumentMeta):
                if not self.document_meta:
                    self.document_meta = self.dict_class()
                self.document_meta.update(value)
            elif isinstance(self.fields[attribute], ResourceMeta):
                if "meta" not in ret:
                    ret["meta"] = self.dict_class()
                ret["meta"].update(value)
            elif isinstance(self.fields[attribute], BaseRelationship):
                if value:
                    if "relationships" not in ret:
                        ret["relationships"] = self.dict_class()
                    ret["relationships"][self.inflect(field_name)] = value
            else:
                if "attributes" not in ret:
                    ret["attributes"] = self.dict_class()
                ret["attributes"][self.inflect(field_name)] = value

        links = self.get_resource_links(item)
        if links:
            ret["links"] = links
        return ret

    @classmethod
    @check_excluded_fields_nullable
    def to_schema_model_dict(cls, exclude_fields=[]):
        """Returns a dict for a SchemaModel in JSON:API format"""
        dict_schema = {
            f: cls._get_field_schema_model_type(f)
            for f in cls._get_fields(
                exclude_fields=exclude_fields + ['ext']
            )
        }

        id_field = dict_schema.pop('id', None)
        if id_field is None:
            raise RequiredFieldExcludedException('id', cls)

        required_fields = cls._get_required_fields(
            exclude_fields=exclude_fields
        )

        return {
            'required': ['data'],
            'properties': {
                "data": {
                    'required': ['type', 'attributes', 'id'],
                    'properties': {
                        "type": {
                            'type': 'string',
                            'default': cls.Meta.type_,
                        },
                        "attributes": {
                            'required': required_fields,
                            'properties': dict_schema,
                            'type': 'object',
                        },
                        "id": id_field,
                    },
                    'type': 'object',
                },
            },
            'type': 'object',
        }


class BaseListRequestSchema(BaseDetailRequestSchema):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, many=True, **kwargs)


class BaseListResponseSchema(BaseDetailResponseSchema):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, many=True, **kwargs)

