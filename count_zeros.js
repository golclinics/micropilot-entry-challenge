const CountZeros = A => {
  let sum = 0;
  A.map(e => ((e == 0) ? sum +=1 : 0));
  return sum;
}
console.log(CountZeros([1,2,0,1,0,0]));
console.log(CountZeros([1,2,0,0]));
console.log(CountZeros([]));
