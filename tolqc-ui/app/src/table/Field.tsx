/*
SPDX-FileCopyrightText: 2023 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

interface Field {
  filter?: boolean,
  filterType?: string|null,
  isAttribute?: boolean|null,
  link?: string|null,
  relationshipBox?: boolean,
  rename?: string|null,
  sort?: boolean,
  type?: string|null,
  width?: number,
}

export interface Fields {
  [key: string]: Field;
}

const fieldDefaults: Field = {
  filter: true,
  filterType: null,
  isAttribute: null,
  link: null,
  relationshipBox: false,
  rename: null,
  sort: true,
  type: null,
  width: 200,
}

export function addFieldDefaults(field: Field) {
  return {
    ...fieldDefaults,
    ...field
  }
}
