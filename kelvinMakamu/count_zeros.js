// Input: Array A
// Returns: count of zeros(0)
// in the array
// [1, 0, 5, 6, 0, 2] ===> 2
// [1, 0, 5, 6, 2] ===> 1
// [1,5, 6, 2] ===> 0
// [0] ===> 1
// [] ==> 0
// [0,0] ==> 2
// [0,1] ==> 1
// [1, 5, 6,9, 2,0] ===> 1
const countZeros = A => {
    let counter = 0;
    for(let i=0;i<A.length;i++){
        if(A[i] === 0){
            counter++;
        }
    }
    return counter;
}

console.log("Total Zeros: ",countZeros([1, 0, 5, 6, 0, 2])," Expected ===> 2");
console.log("Total Zeros: ",countZeros([1, 0, 5, 6, 2])," Expected ===> 1");
console.log("Total Zeros: ",countZeros([1,5, 6, 2])," Expected ===> 0");
console.log("Total Zeros: ",countZeros([0])," Expected ===> 1");
console.log("Total Zeros: ",countZeros([])," Expected ===> 0");
console.log("Total Zeros: ",countZeros([0,0])," Expected ===> 2");
console.log("Total Zeros: ",countZeros([0,1])," Expected ===> 1");
console.log("Total Zeros: ",countZeros([1, 5, 6,9, 2,0])," Expected ===> 1");