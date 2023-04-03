function CountZeros(A){
    let numberOfZeros = 0;
    for(let i of A){
        if(i === 0){
            numberOfZeros++
        }
    }
    return numberOfZeros
}

let arr = [1, 0, 5, 6, 0, 2]

console.log(CountZeros(arr));