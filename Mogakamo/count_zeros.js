numberOfZeros = function (A) {
	var c = 0;
	for (var k in A) {
		if (A[k] === 0 && A[k] === parseInt(A[k], 10)) {
			c += 1;
		}
	}
	return c;
}
