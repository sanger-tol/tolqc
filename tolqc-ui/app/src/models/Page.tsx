/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

export default interface Page {
  name: string;
  auth_required?: boolean;
  admin_only?: boolean;
  ui_element: JSX.Element;
}
