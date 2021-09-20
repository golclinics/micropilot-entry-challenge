function countZeros (arr) {
    let count = 0;
    for (let num of arr) {
        if (num == 0) {
            count++;
        }
    }
    return count;
}


console.log(countZeros([1,2,3,4,5,0,0,0]))