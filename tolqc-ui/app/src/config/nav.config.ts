/*
SPDX-FileCopyrightText: 2026 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import { TNavConfig, PAGE_ACCESS } from "@tol/tol-ui";


export const NAV_CONFIG: TNavConfig = {
  data: {
    "Home": {
      access: PAGE_ACCESS.PUBLIC,
      path: {
        pageElementReference: "home",
        route: "/",
      }
    },
  },
  order:[]
}