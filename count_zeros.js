const myArrays = [9,5,4,0,8,0,2,0,0,0,0,0];
function countZeros(arrays){
const zeros = arrays.filter(array=> array===0);
return zeros.length;
}
countZeros(myArrays);
//loop through the array
//if the integer is equal to 0,i push it in an array variable ie zeros
//get the length of the array
