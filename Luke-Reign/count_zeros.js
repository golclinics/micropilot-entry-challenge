// Write a function CountZeros(A) that takes in an array of integers A, and returns the number of 0's in that array. For example, given [1, 0, 5, 6, 0, 2], the function/method should return 2.

const CountZeros = function (A) {
    let sum = 0;
    A.map(function (B) {
        if (B === 0) {
            sum++;
        } else {
            0;
        }
    })
    return sum;
}
console.log(CountZeros([1, 0, 5, 6, 0, 2])); //2
console.log(CountZeros([1, 0, 5, 6, 0, 2, 0])) //3
console.log(CountZeros([1, 10, 50, 6, 0, 2,])) //1
console.log(CountZeros([1, 5, 6, 2])) //0
console.log(CountZeros([])) //0