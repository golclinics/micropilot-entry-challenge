let a = document.getElementbyId('a');
let b = document.getElementbyId('b');
let c = document.getElementbyId('c');
let calcBtn = document.getElementbyId('calcBtn');
let resultDisplay = document.getElementbyId('resultDisplay');
calcBtn.addEventListener('click', calculate);

function getX(){
    let a1 = a.value;
    let b1 = b.value;
    let c1 = c.value;

    a1 = parseFloat(a1);
    b1 = parseFloat(b1);
    c1 = parseFloat(c1);

    let bPower = Math.pow(b1, 2);
    let fourAC = (4 * a1 *c1);
    let resultToBeSquared = bPower - fourAC;
    let squareRoot =Math.sqrt(resultToBeSquared);
    let bottomOfEquation = (2 * a1);

    if (isNaN(squareRoot) === true){
        resultDisplay.innerHTML = 'non-possible';
    }
    else {
        let result1 = (-b1 - squareRoot) / bottomOfEquation;
        let result2 = (-b1 + squareRoot) / bottomOfEquation;
        resultDisplay.innerHTML = "x = " + result2;
    }
}