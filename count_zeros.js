const test_array = [1, 0, 5, 6, 0, 2]
const challengeFunction = {};
//Using functions
/**
 * Return zero counts in an array
 * @param  {Array} array The array to count
 * @return {Number}      The total number of zero(s) in the array
 */
function count_zeros(array) {
    count = 0
    for (let i = 0; i < array.length; i++){
        count = array[i]==0?(count + 1):count
    }
    return count
}
// console.log(count_zeros(test_array));

challengeFunction.count_zeros = count_zeros;


//using object define properties

// Object.defineProperties(Array.prototype, {
//     count: {
//         value: function(query) {
//             var count = 0;
//             for (let i=0; i < this.length; i++) {
//                 if (this[i]==query){
//                     count=2;
//                 }
//             }
//             return count;
//         }
//     }

// });
// console.log(test_array.count(0))


module.exports = challengeFunction;
