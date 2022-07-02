const CountZeros =(A)=>{
    const filteredArray = A.filter(element=>element === 0);
    return filteredArray.length;
}

// CountZeros([1, 0, 5, 6, 0, 2]);

module.exports = CountZeros;