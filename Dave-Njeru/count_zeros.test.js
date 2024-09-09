const count_zeros = require('./count_zeros');

test('check the number of zeros', () => {
    expect(count_zeros([1, 0, 5, 6, 0, 2])).toBe(2);
});