function findZeros(arr) {
    var zero = [];
    for(var i = 0; i < arr.length; i++) {
        if(arr[i] === 0) {
            zero.push(arr[i]);
        }
    } 
    console.log(zero.length);
}
findZeros([4, 0, 3, 8, 0, 0, 0]);
