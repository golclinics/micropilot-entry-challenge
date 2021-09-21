/*
Instructions:
Write a function CountZeros(A) that takes in an array of integers A, and returns the number of 0's in that array. For example, given [1, 0, 5, 6, 0, 2], the function/method should return 2.
*/

function CountZeros(arr) {
	const input = [...arr];
	const zerosArray = input.filter((n) => n === 0);

	return zerosArray.length;
}

const testData = [1, 0, 5, 6, 0, 2];
console.log(`Zeros detected: ${CountZeros(testData)}`);
