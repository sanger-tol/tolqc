/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import Role from './Role';

export default interface User {
  email: string;
  name: string;
  organisation: string;
  roles: Role[];
}

