/*
SPDX-FileCopyrightText: 2023 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/


export const LoginIcon = (login: any, loginClass: any) => (
  <svg onClick={ login } version="1.2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 100" width="90" height="20">
    <path className={ loginClass } id="login-btn" fillRule="evenodd" d="m10.5 0h429l3.5 2.5c1.9 1.5 4.3 3.8 5.2 5.3 1.6 2.5 1.8 6.3 1.8 42.2 0 37.7-0.1 39.6-2 42.7-1.1 1.8-3.5 4.2-5.3 5.3-3.2 2-5.1 2-217.7 2-212.6 0-214.5 0-217.8-2-1.7-1.1-4.1-3.5-5.2-5.3-1.9-3.1-2-5-2-42.7 0-35.9 0.2-39.7 1.8-42.2 0.9-1.5 3.3-3.8 5.2-5.2zm-7.5 11v78l7.5 7.9h429l7.5-7.9v-78l-8-8h-428zm112.4 8.5c1.2 0.4 2.9 1.6 3.9 2.8 1 1.2 1.8 2.9 1.8 3.9-0.1 1-1.4 3.1-6.1 7.8l-0.5 32.5-0.3-17.3c-0.1-14.6-0.4-17.2-1.7-17.2-0.8 0-2.2-1.1-3-2.3-0.8-1.2-1.5-3.2-1.6-4.4 0-1.3 1.1-3.1 2.7-4.3 1.7-1.3 3.5-1.9 4.8-1.5zm105.9 6.5c2 0 5.1 0.6 6.7 1.5 1.7 0.8 3.7 2.8 4.5 4.5 0.8 1.6 1.5 3.9 1.5 5 0 1.4-0.6 2-2.5 2-1.7 0-2.5-0.6-2.4-1.8 0-1-0.9-2.9-1.9-4.2-1.5-1.9-2.9-2.5-5.7-2.5-2.7 0-4.2 0.6-5.6 2.5-1.1 1.3-2 3.4-2 4.5 0.1 1.1 0.9 2.7 1.8 3.6 1 0.9 4.9 3.1 8.6 4.8 4.7 2.1 7.3 4.1 8.7 6.3 1.1 1.8 2 4.6 2 6.3 0 1.6-0.9 4.4-2 6.2-1.1 1.8-3.6 3.9-5.5 4.8-1.9 0.8-4.6 1.5-6 1.5-1.4 0-4.1-0.7-6-1.5-1.9-0.9-4.4-3-5.5-4.8-1.1-1.8-1.9-4.4-1.7-5.7 0.1-1.8 0.8-2.5 2.2-2.5 1.3 0 2.1 0.9 2.7 3.2 0.5 1.8 1.8 3.9 3.1 4.8 1.2 0.8 3.7 1.5 5.5 1.5q3.3 0 5.8-2.5c1.3-1.4 2.4-3.2 2.4-4 0-0.9-0.5-2.7-1.2-4q-1.3-2.6-8.8-5.9c-4.1-1.8-8-4-8.7-4.7-0.7-0.8-1.6-3.2-1.9-5.4-0.3-2.2-0.1-5.3 0.5-6.8 0.6-1.5 2.6-3.6 4.4-4.7 1.8-1.1 4.9-2 7-2zm70.3 0.2c3.6 0.2 6 1 8.5 2.8 1.9 1.5 4.3 4.4 5.4 6.5 1.6 3.1 2 5.9 2 13 0 7-0.4 9.8-2 12.9-1.1 2.1-3.5 5.1-5.4 6.5-2.2 1.6-5.1 2.7-8 2.9-3.2 0.3-5.8-0.2-8.8-1.7-3-1.5-5.1-3.6-7-6.9-2.5-4.2-2.8-5.7-2.8-13.7 0-8 0.3-9.6 2.8-13.8 1.7-2.9 4.2-5.5 6.5-6.8 2.6-1.4 5.2-1.9 8.8-1.7zm-9 14c-0.9 2.1-1.6 5.4-1.6 7.5 0 2.1 0.3 5.3 0.8 7.2 0.4 1.9 1.7 4.4 3 5.7 1.3 1.5 3.4 2.4 5.2 2.4 1.7 0 3.9-0.5 5-1 1.1-0.6 2.7-2.6 3.5-4.5 0.8-2 1.5-6 1.5-9 0-3.1-0.7-7.1-1.5-9-0.8-2-2.4-4-3.5-4.5-1.1-0.6-3.2-1-4.8-1-1.5 0-3.5 0.5-4.4 1.2-1 0.7-2.4 2.9-3.2 5zm48.4-13.8c3.6 0.3 7 0.9 7.5 1.5 0.6 0.5 0.8 2.5 0.5 4.5-0.4 2.8-0.8 3.5-2 2.9-0.8-0.4-3.5-0.9-6-1.1-2.5-0.3-5.5 0-6.7 0.6-1.3 0.7-3 2.7-3.8 4.7-0.8 1.9-1.5 5.7-1.5 8.5 0 2.7 0.8 6.8 1.8 9.1 0.9 2.3 2.5 4.5 3.5 5 0.9 0.5 3.3 0.9 5.2 0.9 3.4 0 3.5-0.1 3.5-4 0-2.9-0.4-4-1.5-4q-1.5 0-1.5-3c0-3 0.1-3 11-3v9.5c0 9.4 0 9.5-2.7 10.7-1.5 0.6-5.7 1.2-9.3 1.2-5.4 0.1-7.1-0.4-9.9-2.4-1.9-1.4-4.5-4.7-5.8-7.5-1.6-3.7-2.3-6.9-2.3-12 0-5.7 0.5-8.1 2.8-12.5 1.9-4 3.9-6.2 6.7-7.8 3.4-2 5-2.3 10.5-1.8zm-147 0.6h5l0.5 38.5 8.3 0.2c7.2 0.2 8.2 0.5 8 2-0.3 1.5-1.7 1.8-21.8 2.3zm67 0h7v35l14.5 0.5 0.5 7.5h-22zm95 0h7v43h-7zm14.2-0.2l3.5 0.4c3.5 0.3 3.7 0.6 17.3 26.3v-26.5h8v43l-3.2-0.1c-3.2 0-3.5-0.4-10.3-13.5-3.8-7.5-7.3-13.8-7.7-14-0.4-0.2-0.8 5.9-0.8 27.6h-7zm-267.4 10.1c0.2 0 1.1 0.5 2.1 1.1 1.3 0.8 1.7 2.1 1.5 4.7-0.2 2.6 1 6.9 4.2 14.4 2.5 5.9 4 10.8 3.5 10.8-0.6 0-1.3-0.8-1.7-1.8-0.3-0.9-2.3-5.8-4.5-10.7-2.6-6.1-4.5-9.4-6.1-10-1.2-0.6-2.4-2.2-2.5-3.5-0.2-1.6 0.3-3 1.4-3.8 1-0.7 2-1.2 2.1-1.2zm-23.5 2c1.7 0 3.8 1.1 5.5 2.7 2.3 2.5 2.6 3.3 1.4 11.8l9.9 10c5.5 5.5 9.7 10.2 9.4 10.5-0.2 0.3-5.1-4.2-10.7-9.8-9.7-9.8-10.3-10.3-12.7-9.1-2 0.9-3.2 0.9-5.9-0.2-2.3-0.9-3.9-2.5-4.8-4.7-0.9-2.3-1-3.9-0.3-5.7 0.5-1.4 2-3.2 3.2-4 1.3-0.9 3.5-1.5 5-1.5zm66.3 0c1.6 0 2.9 0.8 3.6 2.2 0.6 1.3 0.8 2.8 0.5 3.5-0.3 0.7-1.7 1.7-3.1 2.3-1.8 0.7-3.1 2.6-4.4 6.2-1.1 2.9-2.9 7.4-4 10-1.2 2.6-2.6 4.8-3.1 4.8-0.6 0 1-4.7 3.5-10.5 3.7-8.7 4.3-10.8 3.2-12.1-0.9-1.2-1-2 0-4q1.3-2.4 3.8-2.4zm24.4 5c1.4 0 3.4 0.5 4.3 1.2 0.9 0.7 1.9 2.5 2.2 4 0.5 2.1 0 3.4-1.9 5.3-1.3 1.4-3.2 2.5-4.2 2.5-1 0-2.3-0.4-2.8-1-0.7-0.7-4.4 2.2-11.3 8.7-5.7 5.4-10.5 9.4-10.7 9-0.3-0.4 3.6-4.7 8.6-9.5 5-4.8 9.5-8.8 10-9 0.5-0.1 0.6-1.7 0.1-3.7-0.5-2.7-0.3-3.8 1.2-5.5 1-1.1 3.1-2 4.5-2z"/>
  </svg>
)

export const SearchIcon = () => (
  <svg viewBox="0 0 24 24" width="16px" xmlns="http://www.w3.org/2000/svg">
    <path d="M9,4c2.8,0,5,2.2,5,5s-2.2,5-5,5s-5-2.2-5-5S6.2,4,9,4 M9,2C5.1,2,2,5.1,2,9c0,3.9,3.1,7,7,7s7-3.1,7-7C16,5.1,12.9,2,9,2    L9,2z"/>
    <polygon points="22,20.3 20.3,22 14,15.7 14,14 15.7,14  "/>
    <rect height="3.6" transform="matrix(0.7071 -0.7071 0.7071 0.7071 -5.9741 14.4227)" width="1.2" x="13.8" y="12.6"/>
  </svg>
)

export const InfoIcon = () => (
  <svg width="16px" xmlns="http://www.w3.org/2000/svg" shapeRendering="geometricPrecision" textRendering="geometricPrecision" imageRendering="optimizeQuality" fillRule="evenodd" clipRule="evenodd" viewBox="0 0 512 512">
    <path fillRule="nonzero" d="M256 0c70.69 0 134.7 28.66 181.02 74.98C483.34 121.31 512 185.31 512 256c0 70.69-28.66 134.7-74.98 181.02C390.7 483.34 326.69 512 256 512c-70.69 0-134.7-28.66-181.02-74.98C28.66 390.7 0 326.69 0 256c0-70.69 28.66-134.69 74.98-181.02C121.3 28.66 185.31 0 256 0zm17.75 342.25h29.15v29.32h-93.79v-29.32h28.76v-92.34h-28.76v-29.32h64.64v121.66zm-27.94-150.37c-7.08-.05-13.12-2.53-18.2-7.56-5.08-5.01-7.56-11.11-7.56-18.25 0-7.01 2.48-13.06 7.56-18.08 5.08-5.02 11.12-7.55 18.2-7.55 6.95 0 12.99 2.53 18.08 7.55 5.13 5.02 7.67 11.07 7.67 18.08 0 4.72-1.2 9.07-3.56 12.94-2.36 3.93-5.45 7.07-9.31 9.37-3.87 2.3-8.17 3.45-12.88 3.5zm171.9-97.59C376.33 52.92 319.15 27.32 256 27.32c-63.15 0-120.33 25.6-161.71 66.97C52.92 135.68 27.32 192.85 27.32 256c0 63.15 25.6 120.33 66.97 161.71 41.38 41.37 98.56 66.97 161.71 66.97 63.15 0 120.33-25.6 161.71-66.97 41.37-41.38 66.97-98.56 66.97-161.71 0-63.15-25.6-120.32-66.97-161.71z"/>
  </svg>
)