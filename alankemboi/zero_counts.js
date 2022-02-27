/**
 * 
 * @param {*} A 
 * @returns number
 */

const CountZeros = (A) => {
    var count = 0;
    A.sort();
    for (let i of A) {
        if (i === 0) {
            count++; //count zeros loop
        }
    }
    return count;  //number of zeros
}
var A = [1, 0, 5, 6, 0, 2];

console.log(CountZeros(A))  //2