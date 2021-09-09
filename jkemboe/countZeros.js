//linear time complexity 
const countZero = (A) => {
    //initialize counter to start at 0
    let counter = 0;
    // loop through the array numbers
    for(let count = 0; count < A.length; count++) {
        //check if Array values contains 0 and increment counter on each account
        // return counter if 0 is not found
        (A[count] == 0) ? counter += 1 : counter        
    }
    // return the counter 
    return counter;
}

countZero([1, 0, 5, 6, 0, 2]);


//two test cases each passes hence the algorithm works

// test ('it should return 2 as number of 0's', () => {
    // countZero([1,0,5,6,0,2])
// })

// test ('it should return 1 as number of 0's', () => {
    // countZero([0,5,6,2])
// })

 