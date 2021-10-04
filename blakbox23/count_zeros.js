const countZeros = array => {
    if (!Array.isArray(array)) return ('Please pass a valid array');
    let count = 0;
    array.forEach(element => {
        if (element === 0) {
            count++;
        }
    });
    return count;
}

// console.log(countZeros([]));         //0
// console.log(countZeros([0,1,0,2]));  //2
// console.log(countZeros('A'));        //Please pass a valid array