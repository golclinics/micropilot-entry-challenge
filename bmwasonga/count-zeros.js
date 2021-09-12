let counter = 0;

function CountZeros(A) {
  for (let i = 0; i < A.length; i++) {

       if (A[i] === 0) {
      counter ++;
    }
  }
  return counter;
};

let A = [0, 1,2,0, 3,4,5,0,0,7];
console.log(CountZeros(A));


