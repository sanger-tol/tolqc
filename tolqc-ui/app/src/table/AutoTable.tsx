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
    let searchFilters: object = {};

    // always on filtering - (wildcard or exact)
    if (this.props.fixedFilter !== undefined) {
      searchFilters = this.props.fixedFilter
    }
    // column specific filtering (wildcard)
    if (type === 'filter' && filters !== undefined) {
      // initialising if keys do not exist
      if (!('wildcard' in searchFilters)) {
        searchFilters['wildcard'] = {}
      }
      if (!('exact' in searchFilters)) {
        searchFilters['exact'] = {}
      }
      
      for (const dataField in filters) {
        const filterValue = filters[dataField]['filterVal']
        if (this.props.fields !== undefined && 'dataField' in this.props.fields) {
          const filterType = this.props.fields['dataField']['filterType']
          // TEMP: default to wildcard for a specific field if not defined in fields
          if (filterType === undefined) {
            searchFilters['wildcard'][dataField] = filterValue
          } else {
            searchFilters[filterType][dataField] = filterValue
          }
        // TEMP: wildcard as default for all fields (will soon come from api meta)
        } else {
          searchFilters['wildcard'][dataField] = filterValue
        }
      }
      console.log(searchFilters)
    }
    console.log(type)

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
        
        // error if endpoint doesn't return 200
        if (res.status !== 200) {
          throw Error()
        }

        // check if any data is returned
        if (data[0] !== undefined) {
          let fieldMeta = {};

          // checking if 'fields' has been defined
          if (this.props.fields !== undefined) {
            fieldMeta = structureFieldsUsingProp(this.props.fields)
          } else {
            if ('attributes' in data[0]) {
              const attributes = structureFieldsAuto(data[0].attributes, true)
              fieldMeta = Object.assign(fieldMeta, attributes)
            }
            if ('relationships' in data[0]) {
              const relationships = structureFieldsAuto(data[0].relationships, false)
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
