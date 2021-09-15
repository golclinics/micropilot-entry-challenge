let numberOfZeros = function (arr) {
  let i = 0;
  arr.forEach(function (c) {
    if (c === 0) i++;
  });
  return i;
};

let count = numberOfZeros([1, 0, 5, 6, 0, 2]);

console.log(count);
