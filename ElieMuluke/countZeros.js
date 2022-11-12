module.exports.countZeros = (array) => {
	let count = 0;
	array.forEach((arrayItem) => {
		if (arrayItem === 0) {
			count++;
		}
	});
	return count;
};

// Find test in ElieMuluke\countZeros.test.js
