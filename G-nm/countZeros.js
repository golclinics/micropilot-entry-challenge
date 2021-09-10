const count = (arr) => {
	console.time("countZeros");
	return arr.reduce((acc, curr) => {
		if (curr === 0) {
			return ++acc;
		} else {
			return acc;
		}
	}, 0);
};
console.log(count([10, 12, 0, 0, 2, 3, 0]));

console.timeEnd("countZeros");
module.exports = count;
