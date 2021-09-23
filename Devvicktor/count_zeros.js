"use strict";

const countZeros = (array) => {
  let i = 0;
  array.forEach((element) => {
    if (element === 0) i++;
  });
  return i;
};
console.log(countZeros([1, 0, 5, 6, 0, 2]));
console.log(countZeros([1, 0, 5, 6, 0, 2, 0, 0, 0, 0]));
console.log(countZeros([1, 1, 5, 6, 3, 2]));
