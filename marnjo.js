const getX = (a, b, c) => {
  // this is the squareroot(bsq - 4ac)
  let part1 = Math.sqrt( Math.pow(b, 2) - 4*(a*c) );

  // the -b + part1
  let x1 = (-b + part1) / (2 * a);
  // the -b - part1
  let x2 = (-b - part1) / (2 * a);

  console.log( x1 > x2? x1: x2 );
}

getX(8, 2, -15);
getX(1, 2, -15);

// a8 b2 c-15  1.25 -1.5
// a1 -2b -15c 5 -3