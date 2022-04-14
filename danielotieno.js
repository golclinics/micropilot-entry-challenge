const getX = (a, b, c) => {
  //get the discriminant value
  const discriminant = b * b - 4 * a * c;
  const numerator = Math.sqrt(discriminant);
  const denominator = 2 * a;

  // declare the roots
  let x1;
  let x2;

  if (discriminant < 0) {
    return false;
  } else {
    x1 = (-b + numerator) / denominator;
    x2 = (-b - numerator) / denominator;

    return Math.max(x1, x2);
  }
};

module.exports = getX;
