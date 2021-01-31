const prompt = require("prompt");

prompt.start();

function getX() {
    prompt.get(["a", "b", "c"], (err, res) => {
        try {
            err;
        } catch (err) {
            console.error(err);
        }
        let a = res.a;
        let b = res.b;
        let c = res.c;
        let discriminant = b * b - 4 * a * c;

        if (discriminant > 0) {
            let root1 = (-b + Math.sqrt(discriminant)) / (2 * a);
            let root2 = (-b - Math.sqrt(discriminant)) / (2 * a);

            let x = root1 > root2 ? root1 : root2;
            console.log(x);
        } else if (discriminant == 0) {
            // root1 and root2 are equal
            let root2 = -b / (2 * a);
            let x = (root1 = root2);
            console.log(x);
        } else {
            let realPart = (-b / (2 * a)).toFixed(2);
            let compPart = (Math.sqrt(-discriminant) / (2 * a)).toFixed(2);

            let x = realPart > compPart ? realPart : compPart;
            console.log(x);
        }
    });
}
getX();