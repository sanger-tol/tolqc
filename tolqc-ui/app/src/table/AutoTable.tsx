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
import { Fields } from "./Field";
import { convertTableData,
         convertHeadingData,
         formatDateRange,
         initialiseFilterDict,
         structureFieldsAuto,
         structureFieldsUsingProp,
         switchFilterVisability } from "./TableUtils"


export interface Props {
  endpoint: string,
  fields?: Fields,
  fixedFilter?: object,
  includeNav?: boolean
}

export interface State {
  tableData: any[],
  headings: any[],
  page: number,
  sizePerPage: number,
  totalSize: number,
  error: boolean,
  initialLoad: boolean
}

class AutoTable extends React.Component<Props, State> {
  constructor(props: Props) {
    const headingsDefault = [{
      dataField: '',
      text: ''
    }]
    super(props);
    this.state = {
      tableData: [],
      headings: headingsDefault,
      page: 1,
      sizePerPage: 50,
      totalSize: -1,
      error: false,
      initialLoad: false
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
    let apiFilters: object = {};

    // always on filtering - (contains, exact, range)
    if (this.props.fixedFilter !== undefined) {
      apiFilters = Object.assign(apiFilters, this.props.fixedFilter)
    }

    // column specific filtering
    if (type === 'filter' && filters !== undefined) {
      for (let [key, meta] of Object.entries(filters)) {
        if (meta['filterType'] === 'CONTAINS') {
          apiFilters = initialiseFilterDict(apiFilters, 'contains')
          apiFilters['contains'][key] = meta['filterVal']
        } else if (meta['filterType'] === 'RANGE') {
          apiFilters = initialiseFilterDict(apiFilters, 'range')
          apiFilters['range'][key] = formatDateRange(meta['filterVal'])
        } else if (meta['filterType'] === 'EXACT') {
          apiFilters = initialiseFilterDict(apiFilters, 'exact')
          apiFilters['exact'][key] = meta['filterVal']
        }
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
        filter: apiFilters,
        sort_by: sortField
      }
      })
      .then((res: any) => {
        const apiData = res.data.data
        const apiMeta = res.data.meta
        this.setState({
          page: page,
          sizePerPage: sizePerPage,
          totalSize: apiMeta.total,
          error: false,
        })
        
        // error if endpoint doesn't return 200
        if (res.status !== 200) {
          throw Error()
        }

        // check if any data is returned
        if (apiData[0] !== undefined) {
          let fieldMeta = {};

          // checking if 'fields' has been defined
          if (this.props.fields !== undefined) {
            fieldMeta = structureFieldsUsingProp(this.props.fields, apiMeta.types)
          } else {
            if ('attributes' in apiData[0]) {
              const attributes = structureFieldsAuto(
                apiData[0].attributes,
                apiMeta.types,
                true
              )
              fieldMeta = Object.assign(fieldMeta, attributes)
            }
            if ('relationships' in apiData[0]) {
              const relationships = structureFieldsAuto(
                apiData[0].relationships,
                apiMeta.types,
                false
              )
              fieldMeta = Object.assign(fieldMeta, relationships)
            }
          }
          console.log('data', apiData)
          console.log(fieldMeta)
          console.log(convertTableData(apiData, fieldMeta))
          // only updating heading state on first load
          if (!this.state.initialLoad) {
            this.setState({
              headings: convertHeadingData(fieldMeta),
              initialLoad: true
            })
          }
          this.setState({
            tableData: convertTableData(apiData, fieldMeta)
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
    
    // show nav as default
    let includeNav = this.props.includeNav;
    if (includeNav === undefined) {
      includeNav = true
    }

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
              includeNav={ includeNav }
              noDataIndication={ noDataIndication }
            />
          )
        })()}
      </div>
    );
  }
}

export default AutoTable;
