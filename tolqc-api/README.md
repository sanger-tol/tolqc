<!--
SPDX-FileCopyrightText: 2021 Genome Research Ltd.

SPDX-License-Identifier: MIT
-->

# ToLQC API

## Overview of Directories

### model

Models are sqlalchemy (ORM) classes. These represent SQL concepts in python objects, and produce SQL queries.

### schema

Schemas are from Marshmallow. These serialise models, deserialise requests, and validate deserialised requests.

### swagger

These organise the main namespace of an ORM-model, such as TolqcRun, into a format that is easily documentable by swagger.
They also contain Swagger-models for documentation, and methods to generate them from a schema.

#### A note on _Namespaces_

Namespaces are the delimiters for differing concepts (such as centre/run) within the API, and present themselves
after the prefix (/api/v1) in an endpoint's URL, _e.g._ GET /api/v1/**_centres_**/85.

They originate from flask-restx.

They are listed as the **api** class variable under a swagger class.

### resource

Resources document HTTP methods on namespaces, such as GET, PUT, and POST.

There are two kinds:

- **Detail Resources**
    - Operate only on a single **DB model** instance (_via_ services)
    - An ID must be supplied in the endpoint URL
    - Provide GET, PUT, and DELETE methods
- **List Resources**
    - Operate on multiple instances at a time
    - Do not require an ID in the endpoint URL
    - Provide GET and POST methods

They originate from flask-restx (like namespaces).

### service

Services contain the main backend logic for fulfilling an HTTP request:

- Their methods are called by resources
- They dump and load data using schemas
- They interact with the database using models 

## TODO

- Research how to unify Detail and List schemas into one class
- Get schema validation working, especially concerning required fields
