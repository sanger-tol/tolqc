/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import { format } from 'date-fns'


export function convertToPath(name: string) {
  let path = name.toLowerCase()
  return path.replace(/\s+/g, '-');
}

export function formatDate(text: string) {
  try {
    let date = new Date(text)
    return format(date, 'dd/MM/yyyy HH:mm')
  } catch {
    return text
  }
}

export function stopPropagation(e: { stopPropagation: () => any; }) {
  e.stopPropagation();
}