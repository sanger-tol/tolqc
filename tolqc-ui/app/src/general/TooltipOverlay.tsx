/*
SPDX-FileCopyrightText: 2023 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import React from 'react';
import OverlayTrigger from 'react-bootstrap/OverlayTrigger';
import Tooltip from 'react-bootstrap/Tooltip';


function renderTooltip(contents: JSX.Element|string, props?: any) {
  return(
    <Tooltip 
      id='button-tooltip'
      { ...props }
    >
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
      <OverlayTrigger
        // @ts-ignore
        placement={ placement }
        delay={{ show: 250, hide: 350 }}
        overlay={ renderTooltip(this.props.contents) }
      >
        { this.props.children }
      </OverlayTrigger>
    );
  }
}

export default ToolTipOverlay;
