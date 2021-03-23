function CountZeros(A) {
  let count = 0;
  A.forEach((num) => {
    if (num === 0) {
      count++;
    }
  });
  return count;
}

console.log(CountZeros([1, 0, 5, 6, 0, 2]));
