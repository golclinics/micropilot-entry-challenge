function getX(a, b, c){
    let x1 = ( -b + Math.sqrt( Math.pow(b, 2) - 4*a*c ) )/2*a;
    let x2 = ( -b - Math.sqrt( Math.pow(b, 2) - 4*a*c ) )/2*a;

    return Math.max(x1, x2);
}
