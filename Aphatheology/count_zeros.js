// A function that receives array of numbers and return the occurence of 0

function countZeros(A) {
    
    let count = 0;

    for (let i = 0; i < A.length; i++) {
        if(A[i] === 0) count++;
    }

    return count;
}

console.log(countZeros([1, 0, 5, 6, 0, 2]))