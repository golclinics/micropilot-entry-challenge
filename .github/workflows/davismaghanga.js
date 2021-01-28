function getX(a, b, c) {
    var x1 = (-1 * b + Math.sqrt(Math.pow(b, 2) - (4 * a * c))) / (2 * a);
    var x2 = (-1 * b - Math.sqrt(Math.pow(b, 2) - (4 * a * c))) / (2 * a);
    return Math.max(x1,x2);
}

getX(1,2,-3); //returns 1