const countZeros = (A) => {
  return A.filter((x) => x === 0).length;
};

console.log(countZeros([1, 0, 5, 6, 0, 2]));
