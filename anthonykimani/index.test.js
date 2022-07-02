const CountZeros = require('./index');

test("a function CountZeros() that takes in an array of integers, and returns the number of 0's in that array",()=>{
    const A=[1, 0, 5, 6, 0, 2];
    const number = 0;
    expect(CountZeros(A)).toStrictEqual(filteredArray = A.filter(element=>element===number).length)
});