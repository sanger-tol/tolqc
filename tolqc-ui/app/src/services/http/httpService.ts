// SPDX-FileCopyrightText: 2021 Genome Research Ltd.
//
// SPDX-License-Identifier: MIT

import { createAxiosInstance } from './axios';
import { CONFIG } from './config';
import { AxiosInstance, AxiosRequestConfig } from 'axios';

const authApi = createAxiosInstance(CONFIG);

function normalizeBody(data: unknown) {
  if (!(data instanceof FormData)) {
    if (typeof data === 'object' && data != null) {
      data = JSON.stringify(data);
    }
  }
  return data;
}
function wrapClientWithContext(
  client: AxiosInstance,
  accessToken = '',
) {
  const authHeader = accessToken ? { "api-key": `${accessToken}` } : {};
  const defaultOption = {
    headers: {
      ...CONFIG.headers,
      ...authHeader,
    },
  };

  return {
    get<TResponse = any>(endPoint: string, options: AxiosRequestConfig = {}) {
      return client.get<TResponse>(endPoint, {
        ...defaultOption,
        ...options,
      });
    },
    post<TResponse = any>(
      endPoint: string,
      data: unknown,
      options: AxiosRequestConfig = {},
    ) {
      data = normalizeBody(data);
      return client.post<TResponse>(endPoint, data, {
        ...defaultOption,
        ...options,
      });
    },
    put(endPoint: string, data: unknown, options: AxiosRequestConfig = {}) {
      data = normalizeBody(data);
      return client.put(endPoint, data, {
        ...defaultOption,
        ...options,
      });
    },
    patch(endPoint: string, data: unknown, options: AxiosRequestConfig = {}) {
      data = normalizeBody(data);
      return client.patch(endPoint, data, {
        ...defaultOption,
        ...options,
      });
    },
    delete(endPoint: string, options: AxiosRequestConfig = {}) {
      return client.delete(endPoint, {
        ...defaultOption,
        ...options,
      });
    },
    client,
  };
}

export function httpServices(accessToken = '') {
  return wrapClientWithContext(authApi, accessToken);
}
