const countZeros = require("./countZeros");

test("should return the number of zeros in an array", () => {
	expect(countZeros([10, 12, 0, 0, 2, 3, 0])).toBe(3);
});
