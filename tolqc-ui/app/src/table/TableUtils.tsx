/*
SPDX-FileCopyrightText: 2023 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import { textFilter, customFilter } from 'react-bootstrap-table2-filter';
import DatePicker from './DatePicker';
import { format } from 'date-fns'
import RelationshipLink from './RelationshipLink';
import CellTooltip from './CellTooltip';
import { addFieldDefaults } from './Field';


function isEmptyOrNull(option: string) {
  return option === '' || option === null
}

export function initialiseFilterDict(apiFilters: object, filterType: string) {
  if (!(filterType in apiFilters)) {
    apiFilters[filterType] = {}
  }
  return apiFilters
}

export function formatDateRange(dateRange: string[]) {
  let from = new Date(dateRange[0])
  let to = new Date(dateRange[1])
  from.setHours(0, 0, 0, 0);
  to.setHours(23, 59, 59, 999);
  return {
    from: from,
    to: to
  }
}

export function normaliseCaps(fieldName: string) {
  const words = fieldName.split('_');
  for (let count = 0; count < words.length; count++) {
    words[count] = words[count][0].toUpperCase() + words[count].substring(1);
  }
  return words.join(' ');
}

function checkAndConvertDate(text: string) {
  let date = new Date(text)
  // if num - return text as a num can be converted to date incorrectly
  if (date.toLocaleDateString("en-US") === 'Invalid Date' ||
      !isNaN(Number(text))) {
    return text
  } else {
    const dateText = format(date, 'dd/MM/yyyy')
    const dateContents = format(date, 'dd/MM/yyyy HH:mm')
    return <CellTooltip
      text={ dateText }
      contents={ dateContents }
    />
  }
}

function checkAndAutoConvertText(text: any) {
  try {
    new URL(text) // fails if not link
    // eslint-disable-next-line
    const linkRegEx = /^https?:\/\/([^\/]*).*/
    const imgRegEx = /.*\.(?:png|jpg|jpeg)/i
    if (imgRegEx.test(text.toLowerCase())) {
      return <a href={ text } target="_blank" rel="noopener noreferrer">
        <img src={ text } alt={ text } width="30%"/>
      </a>
    }
    const uiUrl = text.replace(linkRegEx, '$1');
    return <a href={text} target="_blank" rel="noopener noreferrer">
      {uiUrl}
    </a>
  } catch {
    return checkAndConvertDate(text)
  }
}

function createLink(text: any, url: string) {
  return <a href={url} target="_blank" rel="noopener noreferrer">
    {text}
  </a>
}

function formatAttributeData(data: object, fieldMeta: object) {
  const updatedData: object = {}
  for (const [key, value] of Object.entries(data)) {
    if (fieldMeta[key] !== undefined) {
      if (fieldMeta[key].link !== null) {
        const linkField = fieldMeta[key].link
        updatedData[key] = createLink(value, data[linkField])
        continue
      }
    }
    updatedData[key] = checkAndAutoConvertText(value)
  }
  return updatedData
}

function splitRelationshipKeys(fieldMeta: object) {
  const relationshipKeys = {};
  for (let key of Object.keys(fieldMeta)) {
    if (fieldMeta[key]['isAttribute'] === false) {
      const splitKey: string[] = key.split('.')
      relationshipKeys[key] = splitKey
    }
  }
  return relationshipKeys
}

function formatRelationshipData(data: object, fieldMeta: object) {
  const updatedData: object = {}
  const relationshipKeys: object = splitRelationshipKeys(fieldMeta)
  for (const [key, splitKey] of Object.entries(relationshipKeys)) {
    const currentObject = splitKey[0]
    // checking relationship object is correct
    if (data[currentObject] === undefined) {
      throw Error('\'' + key + '\' is not a correct relationship object. ' +
                  'Please check your spelling and pluralisation.')
    }
    // ignoring one-to-many relationships
    if ('data' in data[currentObject]) {
      const headingId = splitKey.join('.')
      updatedData[headingId] = <RelationshipLink
        initialEndpoint={ data[currentObject].links.related }
        relationships={ splitKey }
      />
    } else {
      throw Error(key + ' not in API data call')
    }
  }
  return updatedData
}

export function convertHeadingData(fieldMeta: object) {
  const headerSortingStyle = { backgroundColor: '#edffec' };
  const headerStyling = (width: string) => { return { minWidth: width } }
  const updatedHeadings: object[] = []

  for (const [key, meta] of Object.entries(fieldMeta)) {
    let capsHeading = ''
    let headerWidth = meta.width.toString() + 'px'
    let hidden = false

    // rename via override or normalise a field name
    if (isEmptyOrNull(meta.rename)) {
      capsHeading = normaliseCaps(key)
    } else {
      capsHeading = meta.rename
    }

    if (meta.isAttribute === true) {
      if (key === 'id') {
        headerWidth = '100px'
        hidden = true
      }
      let heading = {
        dataField: key,
        text: capsHeading,
        headerSortingStyle,
        headerStyle: headerStyling(headerWidth),
        hidden: hidden
      }
      if (meta.sort === true) {
        heading['sort'] = true
      }
      if (meta.filter === true) {
        if (meta.filterType === 'RANGE') {
          heading['filter'] = customFilter({
            type: meta.filterType
          })
          heading['filterRenderer'] = (onFilter: any, column: any) =>
            <DatePicker onFilter={ onFilter } column={ column } />
          // temp remove sorting on datetime -> e.stopPropagation()
          heading['sort'] = false
        } else {
          heading['filter'] = textFilter({
            className: 'filter-search-input-hide',
            placeholder: capsHeading,
          })
        }
      }
      updatedHeadings.push(heading);
    
    // if heading is a relationship
    } else if (meta.isAttribute === false) {
      updatedHeadings.push({
        dataField: key,
        text: capsHeading,
        headerSortingStyle,
        headerStyle: headerStyling(headerWidth)
      });
    }
  }
  return updatedHeadings
}

export function convertTableData(data: any[], fieldMeta: object) {
  const updatedData: any[] = []
  data.forEach(row => {
    let fieldData = { 'id': row.id }
    if ('attributes' in row) {
      const attributes = formatAttributeData(row.attributes, fieldMeta)
      fieldData = Object.assign(fieldData, attributes)
    }
    if ('relationships' in row) {
      const relationships = formatRelationshipData(row.relationships, fieldMeta)
      fieldData = Object.assign(fieldData, relationships)
    }
    updatedData.push(fieldData)
  });
  return updatedData;
}

function convertTypeToDefaultFilter(type: string) {
  switch(type) {
    case 'str':
    case 'int':
    case 'float':
      return 'CONTAINS';
    case 'datetime':
      return 'RANGE';
    default:
      return null;
  }
}

// structure fields via the prop 'fields'
export function structureFieldsUsingProp(fields: object, apiFieldMeta: object) {
  for (let [key, meta] of Object.entries(fields)) {
    fields[key] = addFieldDefaults(meta)
    // if key is a relationship
    if (key.includes('.')) {
      if (isEmptyOrNull(meta.rename)) {
        throw Error('Relationship field \'' + key + '\' requires a rename')
      }
      fields[key]['isAttribute'] = false
    } else {
      fields[key]['isAttribute'] = true
      // you can currently only override with 'exact' filtering
      if (fields[key]['filterType'] === 'exact') {
        fields[key]['filterType'] = 'EXACT'
      } else {
        fields[key]['filterType'] = convertTypeToDefaultFilter(apiFieldMeta[key])
      }
    }
  }
  return fields
}

// structure fields using the json-api spec
export function structureFieldsAuto(
  apiFields: object,
  apiFieldMeta: object,
  isAttribute: boolean
) {
  const fields = {}
  // adding internal ID to row
  fields['id'] = addFieldDefaults({
    'rename': 'ID',
    'isAttribute': true
  })
  for (let [key, data] of Object.entries(apiFields)) {
    // ignoring one-to-many relationships
    if (!isAttribute && !('data' in data)) {
      console.warn('\'' + key + '\' is on the many side of the relationship' + 
                    ' - therefore it is being ignored.')
      continue
    }
    fields[key] = addFieldDefaults({
      'isAttribute': isAttribute
    })
    // meta field type is 'data' for attributes
    if (isAttribute) {
      fields[key]['filterType'] = convertTypeToDefaultFilter(apiFieldMeta[key])
    }
  }
  return fields
}

export function switchFilterVisability() {
  let filterVisability = getComputedStyle(document.documentElement).getPropertyValue('--filter-visability')
  if (filterVisability === 'flex') {
    filterVisability = 'none'
  } else {
    filterVisability = 'flex'
  }
  document.documentElement.style.setProperty('--filter-visability', filterVisability);
}
