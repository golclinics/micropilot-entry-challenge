function numberOfZeros(array) {
    var zeros = [];
    for(var i = 0; i < array.length; i++) {
        if(array[i] === 0) {
            zeros.push(array[i]);
        }
    } 
    console.log(zeros.length);
}
numberOfZeros([3, 0, 0, 6, false, true, 0, 4]);