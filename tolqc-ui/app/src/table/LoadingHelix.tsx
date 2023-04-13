/*
SPDX-FileCopyrightText: 2022 Genome Research Ltd.

SPDX-License-Identifier: MIT
*/

const LoadingHelix = () => (
  <div className="d-flex justify-content-center">
    <div className="loader">
      <div className="dna-circle dna-circle1"><i></i></div>
      <div className="dna-circle dna-circle2"><i></i></div>
      <div className="dna-circle dna-circle3"><i></i></div>
      <div className="dna-circle dna-circle4"><i></i></div>
      <div className="dna-circle dna-circle5"><i></i></div>
      <div className="dna-circle dna-circle6"><i></i></div>
    </div>
  </div>
)

export const MiniLoadingHelix = () => {
  return (
    <div className='mini-loader'>
      <LoadingHelix />
    </div>
  )
}

export default LoadingHelix;
