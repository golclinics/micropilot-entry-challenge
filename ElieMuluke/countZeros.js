const countZeros = (array) => {
	let count = 0;
	array.forEach((arrayItem) => {
		if (arrayItem === 0) {
			count++;
		}
	});
	return count;
};

// In case you want to test the code, here is a test function that I created as well

// const assert = (array, expect) => {
// 	const result = countZeros(array);
//     if (result === expect) {
//         console.log(`✅ Test Passed!`);
//     } else {
//         console.log(`❌ Test Passed!`);
//     }
// };

// assert([1, 0, 5, 6, 0, 2], 2);
// assert([1, 2, 3, 4], 0);
// assert([0, 1, 2, 3, 0], 2);
// assert([0, 0, 0], 3);
// assert([1, 2, 3], 0);
