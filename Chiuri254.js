

function getX(a, b, c) {
	// assumption - the function will use numerical values.

	// check is a = 0 which means the equation might be a linear equation dependent on b
	if (a === 0) {
		if (b === 0) {
			return "This is a linear equation";
		}
		else {
			return "Not a quadratic equation"
		}
	}
	// check for distinct roots values for a | b |c 
	if ((b**2 - 4*a*c) < 0) {
		return "No distict roots in the numerical coefficients";
	}


	// declare the variables
	let x1;
	let x2;

	// equate x1 to the computation with (-)
	x1 = (-b - Math.sqrt(b**2 - 4*a*c)) / (2*a);

	// equate x2 to the computation with (+)
	x2 = (-b + Math.sqrt(b**2 - 4*a*c)) / (2*a);

	// check the larger value of X and return it.
	return x1 > x2 ? x1 : x2; 
}