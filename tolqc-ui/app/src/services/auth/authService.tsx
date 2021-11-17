/*
SPDX-FileCopyrightText: 2021 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

import { END_POINT } from '../http/config';
import { httpClient } from '../http/httpClient';

export function getUrlElixirLogin() {
  return httpClient().get(END_POINT.authUrlElixir);
}

export function getToken(dataPost: any) {
  return httpClient().post(END_POINT.authToken, dataPost);
}

export function getProfile(token: string) {
  return httpClient().post(END_POINT.authProfile, {token});
}

export function authLogout() {
  return httpClient().delete(END_POINT.authLogout);
}

//export function getUserPermission() {
//  return httpClient().get(END_POINT.userPermission);
//}