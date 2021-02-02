function getX(a, b, c) {
  // Check if the numbers are empty
  if (!a || !b || !c) {
    return "a, b, c should not be empty";
  }

  // Check if the numbers are not string or float
  if (
    typeof a === "string" ||
    typeof b === "string" ||
    typeof c === "string" ||
    a % 1 !== 0 ||
    b % 1 !== 0 ||
    c % 1 !== 0
  ) {
    return "Only integers are allowed";
  }

  const sqRootItems = Math.pow(b, 2) - 4 * a * c;
  let squareRoot = 0;
  // Check if the sqRootItems are positive or negative
  if (sqRootItems < 0) {
    squareRoot = Math.sqrt(Math.abs(sqRootItems));
  } else {
    squareRoot = Math.sqrt(sqRootItems);
  }

  const addValue = (-b + squareRoot) / (2 * a);
  const subtractValue = (-b - squareRoot) / (2 * a);
  if (addValue > subtractValue) {
    return addValue;
  } else {
    return subtractValue;
  }
}

console.log(getX(1, 5, 6)); // Expected answer is -2

module.exports = getX;
