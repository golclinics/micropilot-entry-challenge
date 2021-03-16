function CountZeroes(A) {
  /* store number of zeroes found */
  let count = 0;

  /* iterate through array of integers A to find zeroes*/
  for (let i = 0; i < A.length; i++) {
    if (A[i] === 0) {
      count++;
    }
  }
  return count;
}

module.exports = CountZeroes;