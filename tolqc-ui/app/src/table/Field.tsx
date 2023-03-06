/*
SPDX-FileCopyrightText: 2023 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

interface Field {
  filter?: boolean;
  isAttribute?: boolean|null;
  link?: string|null;
  rename?: string|null;
  sort?: boolean;
  width?: number;
}

export interface Fields {
  [key: string]: Field;
}

const fieldDefaults: Field = {
  filter: true,
  isAttribute: null,
  link: null,
  rename: null,
  sort: true,
  width: 200,
}

export function addFieldDefaults(field: Field) {
  return {
    ...fieldDefaults,
    ...field
  }
}
