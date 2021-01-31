function getX(a, b, c) {
    let discriminant = b * b - 4 * a * c;

    if (discriminant > 0) {
        let root1 = (-b + Math.sqrt(discriminant)) / (2 * a);
        let root2 = (-b - Math.sqrt(discriminant)) / (2 * a);

        let x = root1 > root2 ? root1 : root2;
        return x;
        // console.log(x);
    } else if (discriminant == 0) {
        // root1 and root2 are equal
        let root2 = -b / (2 * a);
        let x = (root1 = root2);
        return x;
        //  console.log(x);
    } else {
        let realPart = (-b / (2 * a)).toFixed(2);
        let compPart = (Math.sqrt(-discriminant) / (2 * a)).toFixed(2);

        let x = realPart > compPart ? realPart : compPart;
        return x;
        // console.log(x);
    }
}

console.log(`Largest Value of X : ${getX(56, 784, 2)}`);