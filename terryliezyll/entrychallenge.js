function CountZeros(A) {
    let count = 0;
    for (let i = 0; i < A.length; i++) {
        if (A[i] === 0) { 
            count++; 
        }
    }
    return count; // Return the total count of zeros
}
const array = [1, 0, 5, 6, 0, 2];
console.log(CountZeros(array));
const arr = [0, 0, 0, 0, 0, 0];
console.log(CountZeros(arr));