function CountZeros(A){
    // check every element in the array to see if there is a match
    // if there is a match have a count variable to increment
    // return the value of the count variable in the end
    let count = 0
    for (let x = 0; x <= A.length; x++){
        if(A[x] === 0){
            count++;
        };
    };

    return count;
}

const testCase = [1, 0, 5, 6, 0, 2]
console.log(CountZeros(testCase))