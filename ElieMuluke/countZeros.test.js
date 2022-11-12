const { countZeros } = require("./countZeros.js");

// In case you want to test the code, here is a test function that I created as well
const assert = (array, expect) => {
	const result = countZeros(array);
	if (result === expect) {
		console.log(`✅ Test Passed!`);
	} else {
		console.log(`❌ Test Passed!`);
	}
};

assert([1, 0, 5, 6, 0, 2], 2);
assert([1, 2, 3, 4], 0);
assert([0, 1, 2, 3, 0], 2);
assert([0, 0, 0], 3);
assert([1, 2, 3], 0);
