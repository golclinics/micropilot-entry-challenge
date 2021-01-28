function getX(a, b, c) {
  
  //               -b                squareroot of 4ac                 2a
  const x1 = ( ( -1 * b ) + Math.sqrt( Math.pow(b, 2) - (4*a*c) ) ) / (2*a);
  const x2 = ( ( -1 * b ) - Math.sqrt( Math.pow(b, 2) - (4*a*c) ) ) / (2*a);

  return (x1 > x2) ? x1 : x2 ;

}
