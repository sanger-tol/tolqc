/*
SPDX-FileCopyrightText: 2023 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import React from 'react';
import { Tooltip, Whisper } from 'rsuite';


function renderTooltip(contents: JSX.Element|string, props?: any) {
  return(
    <Tooltip>
      { contents }
    </Tooltip>
  );
}

export interface Props {
  contents: JSX.Element|string,
  placement?: string,
  children: JSX.Element
}

export interface State {
}

class ToolTipOverlay extends React.Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = {
    }
  }

  render() {
    let placement = 'auto'
    if (this.props.placement !== undefined) {
      placement = this.props.placement
    }
    return (
      <Whisper
        // @ts-ignore
        placement={ placement }
        controlId="hover-id-click"
        trigger="hover"
        speaker={ renderTooltip(this.props.contents) }
      >
        { this.props.children }
      </Whisper>
    );
  }
}

export default ToolTipOverlay;
