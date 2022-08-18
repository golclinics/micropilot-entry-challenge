// Takes in an array of integers A, and returns the number of 0's in that array.
function CountZeros(A) {
    var count = 0;
    
    for (let i = 0; i < A.length; i++) {
        
        if (A[i] === 0)
            count++;
    }

    return count;
}

