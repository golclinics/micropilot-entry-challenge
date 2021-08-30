//challenge:function that takes in array of integers and returns the number of zero's
let counter = 0;
const CountZeros = (A) => {
  for (let i = 0; i < A.length; i++) {
    if (A[i] === 0) {
      counter += 1;
    }
  }
  return counter;
};
CountZeros(A);
