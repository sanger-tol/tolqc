/*
SPDX-FileCopyrightText: 2021 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import { Role } from './Role';

export interface User {
  email: string;
  name: string;
  organisation: string;
  roles: Role[];
}

