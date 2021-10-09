let A = [];
let i;
let counter = 0;

function CountZeros(A) {
    for (i = 0; i < A.length; i++) {
        if (A[i] === 0) {
            counter = counter + 1;
        }
    }
    return counter;

}
console.log(CountZeros([4, 5, 6, 0, 1, 0, 7, 0, 0]));
