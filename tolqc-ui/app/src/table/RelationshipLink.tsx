/*
SPDX-FileCopyrightText: 2023 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import React from 'react';
import { httpClient } from '@tol/tol-ui'
import ToolTipOverlay from '../general/TooltipOverlay';
import FormatRelationshipTooltip from './FormatRelationshipTooltip';
import { normaliseCaps } from './TableUtils'
import { MiniLoadingHelix } from './LoadingHelix'


export interface Props {
  initialEndpoint: string,
  relationships: string[],
  relationshipBox: boolean
}

export interface State {
  text: JSX.Element|string,
  contents: object
}

class RelationshipLink extends React.Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = {
      text: <MiniLoadingHelix />,
      contents: {}
    }
  }

  componentDidMount() {
    this.handleRelationshipLoading()
  }

  handleRelationshipLoading = async ()  => {
    const { initialEndpoint, relationships } = this.props;
    let attribute = '';
    if (relationships.length !== 1) {
      attribute = relationships.pop()!
    }
    const relationshipTotal = relationships.length
    let endpoint = initialEndpoint

    for (let count = 0; count < relationshipTotal; count++) {
      await httpClient().get(endpoint)
      .then((res: any) => { // eslint-disable-line no-loop-func
        const data = res.data.data
        const attributes = Object.assign({'id': data.id}, data.attributes)
        // if endpoint is the last relationship, set state
        if (count === relationshipTotal-1) {
          // if no requiredFields are set, there is no attribute
          let displayText = ''
          if (attribute === '') {
            displayText = normaliseCaps(data.type) + ': ' + data.id
          } else {
            displayText = attributes[attribute]
          }
          // if defined attribute is incorrect, raise warning
          if (displayText === undefined) {
            this.setState({
              text: 'ERROR: See console',
              contents: { ERROR: 'See console' }
            })
            throw Error('Attribute \'' + attribute + '\' cannot be found in \'' +
                        relationships[count] + '\'')
          }
          this.setState({
            text: displayText,
            contents: attributes
          })
        } else {
          // assign detail endpoint where relationship title is
          const regex = /^\/([^]*)\/.*/
          const endpointObject = relationships[count+1].replace(regex, '$1')
          endpoint = data.relationships[endpointObject]['links']['related']
        }
      })
      .catch((error: any) => {
        console.error(error)
      })
    }
  }

  render() {
    return (
      <div>
        {(() => {
          if (this.props.relationshipBox) {
            return (
              <ToolTipOverlay
                placement='autoHorizontalStart'
                contents={ <FormatRelationshipTooltip contents={ this.state.contents } /> }
              >
                <div className='link-box' key={ this.props.initialEndpoint }>
                  { this.state.text }
                </div>
              </ToolTipOverlay>
            )
          } else {
            return <div>{ this.state.text }</div>
          }
        })()}
      </div>
    );
  }
}

export default RelationshipLink;
