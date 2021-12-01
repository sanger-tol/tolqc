<!--
SPDX-FileCopyrightText: 2021 Genome Research Ltd.

SPDX-License-Identifier: MIT
-->

# Testing

Core - tests the base classes in isolation, as there is a lot of bespoke logic in them
Main - tests the main logic of ToLQC

## Generic Requirements List

- Nullable fields in SQLAlchemy models are not set as required when processed into Swagger OpenAPI models
- Methods requiring auth are not authorized to unauthenticated users, and those without sufficient permissions
- Excluding fields corresponding to non-nullable model-columns in a schema throws an exception
    - Other than id, as this is not required in request schemas
- Specifying an id on post is handled correctly (no 500 INTERNAL SERVER ERROR)
- Requests that lead to sqlalchemy errors do not return 500 INTERNAL SERVER ERROR
