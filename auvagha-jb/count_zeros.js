function CountZeros(A) {
    const zero = 0;

    // Sort array so similar numbers can occur
    // around the same location  
    A.sort();

    // Find the first occurence of zero within the array to 
    // establish a starting point for the loop 
    const firstIndexOfZero = A.indexOf(zero);

    // If not found return -1
    if (firstIndexOfZero == -1) {
        return firstIndexOfZero;
    }

    let count = 0;
    
    // Else run a loop starting from the first index zero occurs 
    // break, when element i is not zero
    for (let i = firstIndexOfZero; i < A.length; i++) {
        if (A[i] != zero) {
            break;
        }
        count++;
    }

    return count;
}