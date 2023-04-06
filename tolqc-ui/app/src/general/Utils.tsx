/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

export function convertToPath(name: string) {
  let path = name.toLowerCase()
  return path.replace(/\s+/g, '-');
}

export function stopPropagation(e: { stopPropagation: () => any; }) {
  e.stopPropagation();
}