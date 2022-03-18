const countZeros = (A) => {
  let count = 0;
  for (let i = 0; i < A.length; i++) {
    if (A[i] === 0) {
      count++;
    }
  }
  return count;
};

console.log(countZeros([1, 0, 3, 7, 6, 0, 5, 3, 9, 0]));
console.log(countZeros([1, 0, 5, 6, 0, 2]));
console.log(countZeros([0, 0, 0]));
