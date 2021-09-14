function CountZeros(A){
    let numOfZeros = 0;
    for(let i = 0; i<A.length; i++){
        if(A[i]===0) numOfZeros++;
    }
    // console.log(numOfZeros);
    return numOfZeros;
}

