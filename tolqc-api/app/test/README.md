<!--
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
-->

# Testing

Base - tests the base classes in isolation, as there is a lot of bespoke logic in them

Main - tests the main logic of ToLQC

## Generic Requirements List

- That id converts from string (in request) to integer (in db) correctly
    - may not be necessary at this stage, as id's don't currently have to comply with JSON:API string requirement
- Make sure that a "many=True" dump behaves properly with ext data

- Nullable fields in SQLAlchemy models are not set as required when processed into Swagger OpenAPI models
- Methods requiring auth are not authorized to unauthenticated users, and those without sufficient permissions
- Excluding fields corresponding to non-nullable model-columns in a schema throws an exception
    - Other than id, as this is not required in request schemas
- Specifying an id on post is handled correctly (no 500 INTERNAL SERVER ERROR)
- Requests that lead to sqlalchemy errors do not return 500 INTERNAL SERVER ERROR
    - e.g. putting and/or posting a foreign key that doesn't exist causes a 400
    - e.g. deleting an instance with dependencies causes a 400
- That every custom exception has a test case!
- That post/put requests lead to the correct corresponding changes to the DB
- That a model, with one of every field, serialiases correctly

- That new list resources work correctly
- That new post response model works correctly
    - check the various edge cases such as:
        - The same object given multiple times
- Test bulk get works correctly
- Responses match their defined Swagger models
- That a list must be specified in a request to a ListResource
- empty lists in ListResource requests return a 400 error
- PUT only accepts a dict, and POST only accepts a list (otherwise 400)
- incorrect data types cause validation errors
- the ext field can't be overwritten by specifying an ext key in a request

- **IMPORTANT** - missing required fields don't raise an DB-integrity 400 error
    - something more specific is raised
