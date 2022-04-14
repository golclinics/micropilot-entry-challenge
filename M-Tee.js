//Quadratic Function
function getX(a, b, c){
    let squareroot = Math.sqrt((b*b) - (4*a*c));
    let divisor = (2*a);
    let x1 = (-b + squareroot)/divisor;
    let x2 = (-b - squareroot)/divisor;

    if(x1 > x2){
        return x1;
    }
    else{
        return x2;
    }
}
//Test case of x^2 – 5x + 6 = 0
console.log(getX(1, -5, 6));