<!--
SPDX-FileCopyrightText: 2021 Genome Research Ltd.

SPDX-License-Identifier: MIT
-->

# ToLQC API

## Design Rationale

### Auto _vs_ Manual Endpoints

- Auto endpoints are generated automatically from model classes, with minimal intervention from a developer, other than configuration in individual files.
- Manual endpoints require most components to be explicitly defined - correct definition is verified at runtime

### setup\_\* Decorators

Every class category, _e.g._ resource or schema, has a mandatory setup\_\* decorator that must be applied to every class.
These serve to either:

- Populate auto classes _or_
- Validate manual classes

### type\_

Every endpoint has an associated type\_. This should be the plural, lower-case form, e.g. _users_.
It is defined on the *model* class for that endpoint (see below).
This is used in several places to identify and fetch the correct classes associated with the endpoint.

## Overview of Directories

### model

Models are sqlalchemy (ORM) classes. These represent SQL concepts in python objects, and produce SQL queries.

### schema

Schemas are from Marshmallow. These serialise models, deserialise (an _individual_) request into a model, and validate a deserialised request.

It is **_very_** important that schemas are instantiated uniquely for each request, and are not shared.

### swagger

These organise the main namespace of an ORM-model, such as TolqcRun, into a format that is easily documentable by swagger.
They also contain Swagger-models for documentation, and methods to generate them from a schema.

#### A note on _Namespaces_

Namespaces are the delimiters for differing concepts (such as centre/run) within the API, and present themselves
after the prefix (/api/v1) in an endpoint's URL, _e.g._ GET /api/v1/**_centres_**/85.

They originate from flask-restx.

They are listed as the **api** class variable under a swagger class.

### resource

Resources document HTTP methods on namespaces, such as GET, PATCH, and POST.

There are two kinds:

- **Detail Resources**
    - Operate only on a single **DB model** instance (_via_ services)
    - An ID must be supplied in the endpoint URL
    - Provide GET, PATCH, and DELETE methods
- **List Resources**
    - Do not require an ID in the endpoint URL
    - Provide (bulk-) GET and POST methods

They originate from flask-restx (like namespaces).

### service

Services contain the main backend logic for fulfilling an HTTP request:

- Their methods are called by resources
- They dump and load data using schemas
- They interact with the database using models

## Additional features

### Extra fields

Models may support extra fields, that are not defined in the schema, by inheriting adding an ExtColumn to the model (named 'ext'),
inheriting the schema from BaseExtSchema, and the Meta class in said schema from BaseExtSchemaMeta

These can be added to, in POST/PATCH requests, by specifying key:value pairs that should be added in the
resource-level meta (see JSON:API spec), in a field named "ext".

## To add a new endpoint

New endpoints can easily be created.

### A default endpoint

For a default endpoint, i.e. one that has all methods, all of which (except GET id/GET bulk) require auth, create:

- A Model
    - Add an ExtColumn (from .base) if you want optional extra fields
- A schema, inheriting from BaseSchema with a meta class inheriting from BaseSchema.BaseMeta
- A swagger, inheriting from BaseSwagger
- A service, inheriting from BaseService
- A list and detail resource (or just a choice of one), inheriting from
BaseListResource and BaseDetailResource respectively

Finally the entire api (from the resource file) should be added to the
blueprint in route/api.py .

(At the time of writing) Centre is the canonical example of a default endpoint - follow its structure.

### A bespoke endpoint

Bespoke endpoints do not need to (and probably shouldn't) inherit from the base classes.

## Limitations

- Compound/composite keys are not supported
- Model tablenames must be plural
    - This is because the endpoint and "JSON:API Resource type" is equal to this

It is worth noting that these limitations can be overcome by hardcoding the various classes for an endpoint,
instead of inheriting from the base classes and letting them dynamically generate the details.
