// SPDX-FileCopyrightText: 2021 Genome Research Ltd.
//
// SPDX-License-Identifier: MIT

import { httpServices } from './httpService';
import { getTokenFromLocalStorage } from '../localStorage/localStorageService';

//let initInterceptors = false;

export function httpClient() {
  const token = getTokenFromLocalStorage();
  const { client, ...http } = httpServices(token);
  return http;
}
