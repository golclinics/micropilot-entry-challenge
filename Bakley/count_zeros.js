function CountZeros(A) {
     const count = A.filter(zero_count => {
        return zero_count === 0;
    });

    return count.length
};

console.log(CountZeros([1,0,5,6,0,2]))
console.log(CountZeros([4, 0, false, 5, 0]))
console.log(CountZeros([1, 1, 2, 3, 5, 8, 13]))
