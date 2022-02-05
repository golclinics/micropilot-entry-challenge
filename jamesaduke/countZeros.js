/**
 * Write a function CountZeros(A) that takes in an array of integers A, and returns the number of 0's in that array. For example, given [1, 0, 5, 6, 0, 2], the function/method should return 2.
 */

const CountZeros = (A) => {
    let count = 0;
    for (let i = 0; i < A.length; i++) {
        if (A[i] === 0) {
        count++;
        }
    }
    return count;
}

console.log(CountZeros([1, 0, 5, 6, 0, 2]));
console.log(CountZeros([1, 0, 5, 6, 0, 2, 0]));
console.log(CountZeros([1, 0, 5, 6, 0, 2, 0, 0]));
console.log(CountZeros([0, 0, 0]));