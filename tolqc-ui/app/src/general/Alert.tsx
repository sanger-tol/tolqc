/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import { Alert as AlertBootstrap } from "react-bootstrap";

export interface AlertProps {
  type: string
  message: string
}

function Alert(props: AlertProps) {
  return (
    <AlertBootstrap key={props.type} variant={props.type}>
      {props.message}
    </AlertBootstrap>
  );
}

export default Alert;
