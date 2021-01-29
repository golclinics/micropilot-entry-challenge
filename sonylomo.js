function getX(a, b, c) {
  /** check if values entered aren't numbers */
  if (typeof a !== "number" || typeof b !== "number" || typeof c !== "number") {
    return "Please enter a number.";
  }

  /**value that holds greater root */
  let greaterRoot;

  /**calculate discriminant */
  const squareroot = Math.sqrt(b * b - 4 * a * c);

  /** quadratic roots*/
  const root1 = (-b + squareroot) / (2 * a);
  const root2 = (-b - squareroot) / (2 * a);

  /** check if roots are equal */
  if (root1 === root2) {
    return "roots are equal";
  }
  /**check if root is not a number */
  if (isNaN(root1) || isNaN(root2)) {
    return "indefinite roots";
  }
  /**checks for the root that's greater  */
  greaterRoot = root1 > root2 ? root1 : root2;

  return greaterRoot;
}

//if greater
getX(1, 6, 5);

//if equal
getX(1, -6, 9);

//if squareroot < 0
getX(1, -3, 10);
