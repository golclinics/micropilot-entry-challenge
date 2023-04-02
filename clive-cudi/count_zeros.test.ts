const { CountZeros: countZeros} = require("./count_zeros");

describe('countZeros', () => {
  test('returns 0 when given an empty array', () => {
    expect(countZeros([])).toBe(0);
  });

  test('returns 0 when given an array with no zeros', () => {
    expect(countZeros([1, 2, 3])).toBe(0);
  });

  test('returns 1 when given an array with a single zero', () => {
    expect(countZeros([0])).toBe(1);
  });

  test('returns the correct count when given an array with multiple zeros', () => {
    expect(countZeros([1, 0, 5, 6, 0, 2])).toBe(2);
  });

  test('returns the correct count when given an array with all zeros', () => {
    expect(countZeros([0, 0, 0, 0, 0])).toBe(5);
  });
});
