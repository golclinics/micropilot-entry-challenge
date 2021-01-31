function getX(a, b, c) {
  let res1, res2;
  let det = b * b - 4 * a * c;

  //check for different states

  //if the upper part is zero, the roots will be equal
  if (det == 0) {
    res1 = -b / (2 * a);
    res1 = res2;
    console.log(`both roots are ${res2}`);
    return res1;
  } else if (det > 0) {
    //if greater than 0, then it will have 2 roots
    res1 = (-b + Math.sqrt(det)) / (2 * a);
    res2 = (-b - Math.sqrt(det)) / (2 * a);

    const roots = [res1, res2];
    const maxRoot = Math.max(...roots);
    console.log(`maxroot is ${maxRoot} from ${res2} and ${res1}`);
    return maxRoot;
  } else {
    console.log("the equation has no real roots");
  }
}

getX(6, 11, -35);
