const countZeros = require("./count_zeros")

test("check number of zeros in the array",() =>{
    const array = [1, 0, 5, 6, 0, 2];
    expect(countZeros(array)).toBe(2);
});

test("check array with no zeros",() =>{
    const array2 = [1, 5, 6, 2];
    expect(countZeros(array2)).toBe(0);
});

test("check if array is empty",() =>{
    const array3 = [];
    expect(countZeros(array3)).toBe(0);
});