function CountZeros(A){
    let count = 0;
    A.forEach(element => {
        if(element === 0){
            count++;
        }
    });
    return count;
}