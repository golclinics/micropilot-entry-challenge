let arr = [1,0,2,4,6,0,5,6,9,0];

function countZeros(arr, value) {
     let count = 0;
     for (let i = 0; i<arr.length; i++) {
         if (arr[i] === value) {
             count++;
         }
     }
     return count;
}
console.log(countZeros([1,0,2,4,6,0,5,6,9,0], 0));
