function count_zeros(A) {
    let count = 0
    for (let number in A) {
        if (A[number] === 0 && A[number] === parseInt(A[number], 10)) {
            count += 1
        }   
    }
    return count;
}

// testing the program with the provided array
if (require.main === module) {
    console.log("Expecting: 2")
    console.log("=>", count_zeros([1,0,5,6,0,1]))
}