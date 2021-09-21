const CountZeros = (A) => {
    let count = 0
        for(let i=0; i < A.length; i++){
            if(A[i] === 0){
                count++
            }
        }
    console.log(count)
    return count
}


const testArray = [1, 0, 5, 6, 0, 2]


CountZeros(testArray)

