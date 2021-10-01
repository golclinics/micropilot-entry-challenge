function CountZeros(A) {
    no_zeros = 0;
    for (let i = 0; i < A.length; i++) {
        if (A[i] === 0) {
            no_zeros++;
        }
    }
    return no_zeros;
}