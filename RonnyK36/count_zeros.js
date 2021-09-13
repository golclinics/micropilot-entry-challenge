// a function to count the occurence of zeros(0) in a list

let A = [1, 4, 9, 0, 6, 2, 8, 0, 6, 4, 0, 3, 7];

let counter = 0;

// function taking in A and counting number of zeros
const CountZeros = (A) => {
    for (let i = 0; i < A.length; i++) {
        if (A[i] === 0) {
            counter += 1;
        }
    }
    return counter;
};

// show the result
console.log(CountZeros(A));