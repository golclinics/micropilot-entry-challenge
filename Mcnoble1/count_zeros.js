// Write a function CountZeros(A) that takes in an array of integers A, 
// and returns the number of 0's in that array. For example, given [1, 0, 5, 6, 0, 2], 
// the function/method should return 2.

let arrayOfIntegers = [];
let zeroCount = 0;
function countZeros(arrayOfIntegers) {
    for (let i = 0; i < arrayOfIntegers.length; i++) {
        if (arrayOfIntegers[i] === 0) {
            zeroCount += 1;
        }
    }
    return zeroCount;
}

console.log(countZeros([1, 0, 5, 6, 0, 0, 2]));