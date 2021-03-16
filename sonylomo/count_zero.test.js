const CountZeroes = require("./count_zero");

test("counts the number of zeroes in array", () => {
  const testArray1 = [1, 0, 5, 6, 0, 2];
  expect(CountZeroes(testArray1)).toBe(2);
});

test("array is not empty", () => {
  const testArray2 = [1, 0, 5, 6, 0, 2];
  expect(testArray2.length).toBeGreaterThan(0);
});

test("array has no zeroes", () => {
  const testArray3 = [5, 6, 7, 8];
  expect(CountZeroes(testArray3)).toBe(0);
});
