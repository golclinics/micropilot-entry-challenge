// Write a function CountZeros(A) that takes in an array of integers A,
//  and returns the number of 0's in that array. For example, given [1, 0, 5, 6, 0, 2], the function/method should return 2

  let  CountZeros=function(array){
    return  array.filter(v => v === 0).length;
}

console.log(CountZeros( [1,9,0,8,0,0]))
