const CountZeros = (numberArray) => {
  let count = 0;
  numberArray.map((x) => {
    if (x === 0) {
      count += 1;
    }
  });
  console.log(count);
};
