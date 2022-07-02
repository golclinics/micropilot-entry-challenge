
//PSEUDOCODE
/* The function takes an array of intergers and uses the filter method to filter out elements,
that are not equal to the number zero , using a strict equality operator .Then uses the length method to get the number
of 0's in the array and returns the output.*/

//a function CountZeros() that takes in an array of integers, and returns the number of 0's in that array
const CountZeros =(A)=>{
    const filteredArray = A.filter(element=>element === 0);
    return filteredArray.length;
}

CountZeros([1, 0, 5, 6, 0, 2]);

module.exports = CountZeros;