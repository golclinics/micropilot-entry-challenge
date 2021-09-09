/* Write a function CountZeros(A) that takes in an array of integers A,
 and returns the number of 0's in that array. For example,
 given [1, 0, 5, 6, 0, 2], the function/method should return 2.*/

let A = [3, 6, 0, 6, 9, 0, 2, 4, 1, 0, 5, 0];

let counter = 0;

const CountZeros = (A) => {
    for (let i = 0; i < A.length; i++) {
        if (A[i] === 0) {
            counter += 1;
        }
    }
    return counter;
};
console.log(CountZeros(A));