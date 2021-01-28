

/*I'll try to make it as readable as I can */

function getX(a, b, c) {
    //this get the -b in the equation
    //the -b part is then added to the squareroot part

    const x1 = ((-1 * b) + Math.sqrt(Math.pow(b, 2) - (4 * A * c))) / (2 * a);
    const x2 = ((-1 * b) + Math.sqrt(Math.pow(b, 2) - (4 * A * c))) / (2 * a);

    //checks if a is equal to zero

    if (a === 0) {
        throw ("equation is linear")
    }

    //checks if x1 is greater that x2, if so it console logs x1 
    //otherwise x2 is logged in the console
    console.log(x1 > x2 ? x1 : x2)
}