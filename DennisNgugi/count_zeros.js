function countZeros(A) {
    /* set a counter to store the number of zeros found */
    let counter = 0;
    /* iterate through array of integers A to find zeroes*/
    for (let i = 0; i < A.length; i++) {
      if (A[i] === 0) {
        counter++;
      }
    }
    return counter;
  }
module.exports = countZeros;
