let root1;
let root2;

//for node.js
// const prompt = require('prompt-sync')();

console.log("Input a, b and c from the equation\nax2 + bx + c = 0, where\na, b and c are real numbers and\na≠ 0 ");
let a = prompt("Input \"a\":");
let b = prompt("Input \"b\":");
let c = prompt("Input \"c\":");

//calculate roots
let disc = b * b - 4 * a * c;

if (disc > 0) {
    root1 = (-b + Math.sqrt(disc)) / (2 * a);
    root2 = (-b - Math.sqrt(disc)) / (2 * a);
    if (root1 > root2) {
        console.log(`x = ${root1}`);
    } else {
        console.log(`x = ${root2}`);
    }
} else if (disc == 0) {
    root1 = root2 = -b / (2 * a);
    console.log(`x = ${root1}`);
} else {
    let real = (-b / (2 * a)).toFixed(2);
    let unreal = (Math.sqrt(-disc) / (2 * a)).toFixed(2);
    console.log(`x = ${real}±${unreal}i`)
}