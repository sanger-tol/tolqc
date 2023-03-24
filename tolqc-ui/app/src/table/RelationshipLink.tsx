/*
SPDX-FileCopyrightText: 2023 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import React from 'react';
import { httpClient } from '@tol/tol-ui'
import ToolTipOverlay from '../general/TooltipOverlay';
import LoadingHelix from './LoadingHelix';
import { normaliseCaps } from './TableUtils'


function convertRelationshipData(contents: object|string) {
  return (
    <div>
      {Object.entries(contents).map(([key, value]) => (
        <div className='relationship-tooltip' key={ key }>
          <span className='tooltip-key'>{ normaliseCaps(key) }:</span>
          <span className='tooltip-value'>{ value }</span>
        </div>
      ))}
    </div>
  );
}

const MiniLoader = () => {
  return (
    <div className='mini-loader'>
      <LoadingHelix />
    </div>
  )
}

export interface Props {
  initialEndpoint: string,
  relationships: string[]
}

export interface State {
  text: JSX.Element|string,
  contents: object
}

class RelationshipLink extends React.Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = {
      text: <MiniLoader />,
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
        // if endpoint is the last relationship, set state
        if (count === relationshipTotal-1) {
          // if no requiredFields are set, there is no attribute
          let displayText = ''
          if (attribute === '') {
            displayText = normaliseCaps(data.type) + ': ' + data.id
          } else {
            displayText = data.attributes[attribute]
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
            contents: data.attributes
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
      <ToolTipOverlay
        placement='bottom'
        contents={ convertRelationshipData(this.state.contents) }
      >
        <div className='link-box' key={ this.props.initialEndpoint }>
          { this.state.text }
        </div>
      </ToolTipOverlay>
    );
  }
}

export default RelationshipLink;
