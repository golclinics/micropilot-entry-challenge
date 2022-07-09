'use strict';
const myArray = [1, 0, 5, 6, 0, 2,9,0];

const countZeros = function(array) {
    let count = 0;
    array.forEach(element => {
        if(element === 0) {
            count = count + 1;
        }
    })
    return count;
}

let result = countZeros(myArray);
console.log(result);