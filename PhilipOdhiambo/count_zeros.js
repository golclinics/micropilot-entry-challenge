function countZeros(A) {
    let numArr = [];
    numArr = A;
    return numArr.filter(item => item == 0).length;
}