function count_zeros(A) {
    let count = 0;
    for (let i = 0; i < A.length; i++) {
        if(A[i] === 0) {
            count++;
        }
    }
    return count;
}
//export function
module.exports = count_zeros;