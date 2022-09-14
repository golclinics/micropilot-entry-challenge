const { describe } = require("jest-circus");
const countZeros = require("./countZeros");

describe("COUNT ZEROS TEST CASES", () => {
  test("If array is empty zero should be returned", () => {
    expect(countZeros([])).toBe(0);
  });

  test("Number of zeros returned should be accurate", () => {
    expect(countZeros([0])).toBe(1);
    expect(countZeros([1, 0, 5, 6, 0, 2])).toBe(2);
    expect(countZeros([0, 0, 0, 0, 0, 0])).toBe(6);
    expect(countZeros([1, 8, 5, 6, 9, 2])).toBe(0);
  });
});
