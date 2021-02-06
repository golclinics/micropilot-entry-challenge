function getX(a, b, c) {
    let x1 = (-b + Math.sqrt(Math.pow(b, 2) - 4 * a * c)) / (2 * a);
    let x2 = (-b - Math.sqrt(Math.pow(b, 2) - 4 * a * c)) / (2 * a);
  
    if (x1 > x2) {
      return x1;
    } else {
      return x2;
    }
  }
  console.log(getX(1, 5, 6));