<!--
SPDX-FileCopyrightText: 2021 Genome Research Ltd.

SPDX-License-Identifier: MIT
-->

# ToLQC API

## Overview

### (Database) Models

Models are sqlalchemy (ORM) classes. These represent SQL concepts in python objects, and produce SQL queries.

### Schemas

Schemas are from Marshmallow. These are the intermediate forms between json requests and DB models.

There are (currently) two kinds:

- Request schemas
    - deserialises user-supplied input
    - provide this to DB models
- Response schemas
    - receives data back from the models, after the queries have taken place
    - serialises this data in [**JSON:API**](https://jsonapi.org) format

### Namespaces

Namespaces are the delimiters for differing concepts (such as centre/run) within the API, and present themselves
after the prefix (/api/v1) in an endpoint's URL, _e.g._ GET /api/v1/**_centres_**/85.

They originate from flask-restx.

### Resources

Resources provide HTTP methods on namespaces, such as GET, PUT, and POST.

There are two kinds:

- **Detail Resources**
    - Operate only on a single **DB model** instance (_via_ schemas)
    - An ID must be supplied in the endpoint URL
    - Provide GET, PUT, and DELETE methods
- **List Resources**
    - Operate on multiple instances at a time
    - Do not require an ID in the endpoint URL
    - Provide POST methods

They originate from flask-restx (like namespaces).

## Dataflow

1. User-input to endpoint
2. Received by a **resource** on the relevant **namespace**
3. Validated by a **request schema**
4. Passed to a **DB model**
5. The database is queried appropriately
6. Returned data (if any) is passed to a **response schema**, and formatted
7. The resource then serves the formatted data to the end-user in a response
