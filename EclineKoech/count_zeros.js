// Write a function CountZeros(A) that takes in an array of integers A, and returns the number of 0's in that array. For example, given [1, 0, 5, 6, 0, 2], the function/method should return 2.
let intA = [1, 0, 5, 6, 0, 2,0];
let int2 = [0,0,0,0];

function countZeros(intA){
  let intCount = [];
  for(let i = 0; i < intA.length; i++){
    if(intA[i] == 0){
      intCount.push(intA[i]);
    }
  }
  console.log(`The number of zeros is ${intCount.length}`);
}
 countZeros(intA);
 countZeros(int2);
