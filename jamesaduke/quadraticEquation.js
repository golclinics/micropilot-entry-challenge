/**
 * Given a, b, c for a quadratric expression ax2 + bx + c = 0. Write a function getX that returns the larger of the values for X, i.e. if x1 = -2 and x2 = 5, getX should return 5
 */

const getX = (a, b, c) => {
    let x1, x2;
    let discriminant = Math.pow(b, 2) - 4 * a * c;

    if (discriminant > 0) {
        x1 = (-b + Math.sqrt(discriminant)) / (2 * a);
        x2 = (-b - Math.sqrt(discriminant)) / (2 * a);
        return x1 > x2 ? x1 : x2;
    } else if (discriminant == 0) {
        x1 = x2 = -b / (2 * a);

        return x1 > x2 ? x1 : x2;
    } else {
        let realPart = (-b / (2 * a)).toFixed(2);

        // result
        return realPart;
    }
}

// console.log(getX(1, 2, 3)); // -1
console.log(getX(1,6,5));
console.log(getX(10,8,9));
