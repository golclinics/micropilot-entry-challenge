function countZeros(numbers) {
	let count = 0;

	for (let number of numbers) {
		if (number === 0) {
			count += 1;
		}
	}

	return count;
}


// const numbers = [1, 0, 5, 6, 0, 2];
// const zeroCount = countZeros(numbers); // 2
// console.log(`[1, 0, 5, 6, 0, 2] = ${zeroCount}`);
