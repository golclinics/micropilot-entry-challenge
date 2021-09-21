function countZeros(A){
    let count = 0;

    A.forEach(item => {
        if(item == 0){
            count += 1;
        }
    })

    return count;
}


