/**
 * Find the roots of a quadratic equation.
 * If the roots are real numbers, return the maximum of the two roots.
 * If the roots are complex numbers, return the string equivalent of the complex numbers.
 *
 * @param {number} a Independent variable 'a'
 * @param {number} b Independent variable 'b'
 * @param {number} c Independent variable 'c'
 * @returns {number|string} The maximum number of the two roots or complex number string values or error message
 */
function getX(a, b, c) {
  // Check if the independent variables 'a', 'b', and 'c' are not finite numbers; return an appropriate message
  if (!isFinite(a) || !isFinite(b) || !isFinite(c)) {
    return `Please enter a finite number for each independent variable 'a', 'b', and 'c'`;
  }

  // Check if the independent variable 'a' is zero; return an appropriate message
  if (a === 0) {
    return `Please enter a finite number other than zero for the independent variable 'a'`;
  }

  const discriminant = b * b - 4 * a * c; // The discriminant term of the quadratic equation
  const denominator = 2 * a; // The denominator of the quadratic equation
  let output;

  if (discriminant > 0) {
    // The discriminant is greater than zero: the roots will be two different real numbers
    const firstRoot = (-b + Math.sqrt(discriminant)) / denominator;
    const secondRoot = (-b - Math.sqrt(discriminant)) / denominator;
    output = Math.max(firstRoot, secondRoot);
  } else if (discriminant === 0) {
    // The discriminant is equal to zero: the roots will be two equal real numbers
    output = -b / denominator;
  } else {
    // The discriminant is less than zero: the roots will be two different complex numbers
    const realNum = -b / denominator;
    const imaginaryNum = Math.sqrt(-discriminant) / denominator;
    output = `${realNum} + ${imaginaryNum}i or ${realNum} - ${imaginaryNum}i`;
  }

  return output;
}
