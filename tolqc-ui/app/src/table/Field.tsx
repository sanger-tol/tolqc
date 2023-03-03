/*
SPDX-FileCopyrightText: 2023 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

interface Field {
  filter?: boolean;
  link?: string|null;
  rename?: string|null;
  sort?: boolean,
  type?: string,
  width?: number;
}

export interface Fields {
  [key: string]: Field;
}

const fieldDefaults: Field = {
  filter: true,
  link: null,
  rename: null,
  sort: true,
  type: 'attribute',
  width: 200,
}

export function addFieldDefaults(field: Field) {
  return {
    ...fieldDefaults,
    ...field
  }
}
