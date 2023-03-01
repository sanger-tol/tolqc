/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import React from "react";
import { httpClient } from '@tol/tol-ui'
import Table from "./Table";
import LoadingHelix from "./LoadingHelix";
import NoDataAlert from "./NoDataAlert";
import TableErrorAlert from './TableErrorAlert';
import { convertTableData,
         convertHeadingData,
         structureFieldData,
         switchFilterVisability } from "./TableUtils"


export interface Props {
  endpoint: string,
  requiredFields?: object
}

export interface State {
  tableData: any[],
  headings: any[],
  relationships: any,
  page: number,
  sizePerPage: number,
  totalSize: number,
  error: boolean
}

class AutoTable extends React.Component<Props, State> {
  constructor(props: Props) {
    const headings_default = [{
      dataField: '',
      text: ''
    }]
    super(props);
    this.state = {
      tableData: [],
      headings: headings_default,
      relationships: {},
      page: 1,
      sizePerPage: 50,
      totalSize: -1,
      error: false
    }
  }

  refreshPagination = () => {
    const { page, sizePerPage } = this.state;
    this.handleTableChange('pagination', { page: page, sizePerPage: sizePerPage })
  }

  componentDidMount() {
    this.refreshPagination()
  }

  handleTableChange = (type: string, { page, sizePerPage, filters, sortOrder, sortField } : {
    page: number,
    sizePerPage: number,
    filters?: object,
    sortOrder?: string,
    sortField?: string
  }) => {
    let searchFilters: string = '';

    // filtering
    if (type === 'filter') {
      searchFilters = '['
      for (const dataField in filters) {
        const filterVal: string = filters[dataField]['filterVal'];
        searchFilters += dataField + '==\'' + filterVal + '\','
      }
      searchFilters = searchFilters.slice(0, -1)
      if (searchFilters.length !== 0) {
        searchFilters += ']'
      }
    }

    // sorting
    if (sortOrder === 'desc') {
      sortField = '-' + sortField
    }

    // get data and update state
    httpClient().get('/' + this.props.endpoint, { 
      params: {
        page: page,
        page_size: sizePerPage,
        filter: searchFilters,
        sort_by: sortField
      }
      })
      .then((res: any) => {
        const data = res.data.data
        const meta = res.data.meta
        this.setState({
          page: page,
          sizePerPage: sizePerPage,
          totalSize: meta.total,
          error: false,
        })

        // check if any data is returned
        if (typeof data[0] !== 'undefined') {
          let fieldMeta = {};

          // checking if the fields have been defined
          if (typeof this.props.requiredFields !== 'undefined') {
            fieldMeta = structureFieldData(this.props.requiredFields)
          } else {
            if ('attributes' in data[0]) {
              const attributes = structureFieldData(data[0].attributes,
                                                    'attribute')
              fieldMeta = Object.assign(fieldMeta, attributes)
            }
            if ('relationships' in data[0]) {
              const relationships = structureFieldData(data[0].relationships,
                                                       'relationship')
              fieldMeta = Object.assign(fieldMeta, relationships)
            }
          }
          this.setState({
            tableData: convertTableData(data, fieldMeta),
            headings: convertHeadingData(fieldMeta)
          })
        }
      })
      .catch((error: any) => {
        console.error(error)
        this.setState({
          error: true
        })
      }
    )
    this.setState(() => ({
      tableData: [],
      totalSize: this.state.totalSize
    }));
  }

  render() {
    const { tableData, headings, page, sizePerPage, totalSize, error } = this.state;

    return (
      <div>
        {(() => {
          let noDataIndication: JSX.Element;
          if (error) {
            noDataIndication = <TableErrorAlert />
          } else if (totalSize === 0) {
            noDataIndication = <NoDataAlert />
          } else {
            noDataIndication = <div className='p-5'>
                <LoadingHelix />
              </div>
          }
          return (
            <Table
              data={ tableData }
              columns={ headings }
              onTableChange={ this.handleTableChange }
              onFilterButton={ switchFilterVisability }
              page={ page }
              sizePerPage={ sizePerPage }
              totalSize={ totalSize }
              noDataIndication={ noDataIndication }
            />
          )
        })()}
      </div>
    );
  }
}

export default AutoTable;
