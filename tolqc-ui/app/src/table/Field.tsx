/*
SPDX-FileCopyrightText: 2023 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

interface Field {
  name?: string|null;
  filter?: boolean;
  link?: string|null;
  width?: number;
}

export interface Fields {
  [key: string]: Field;
}

const fieldDefaults: Field = {
  name: null,
  filter: true,
  link: null,
  width: 300,
}

export function addFieldDefaults(field: Field) {
  return {
    ...fieldDefaults,
    ...field
  }
}
