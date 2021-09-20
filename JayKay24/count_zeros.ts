/**
 * Returns the total number of zeros in the array
 * @param {number[]} integers - integer array (sorted / unsorted)
 * @returns {number} totalZeros - total count of zeros in the array
 */
function CountZeros(integers: number[]): number {
  let totalZeros = 0;

  for (const int of integers) {
    if (int === 0) {
      totalZeros++;
    }
  }

  return totalZeros;
}
