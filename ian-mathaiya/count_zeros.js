//The code below uses the filter array method to...
//...count the number of Zeros(0s) in the array(x) below
let x = [10, 2, 0, 204, 0, 17, 0, 528, 983, 0, 98, 0, 1006, 0, 39].filter(function (count_zeros) { return count_zeros === 0 }).length
console.log(x)