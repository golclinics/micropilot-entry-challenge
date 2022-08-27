const challenge = require('../count_zeros.js');

const { count_zeros } = challenge;
const maybe = count_zeros === undefined ? test.skip : test;
console.log(typeof maybe)

maybe('Challenge - 1 : my count_zeros function can count zeros in an array', () => {
    const numbers = [
        1, 
        0, 
        5, 
        6, 
        0, 
        2,
        0
    ];
    expect(count_zeros(numbers)).toBe(3);
});