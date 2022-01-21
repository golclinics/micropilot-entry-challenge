var arr = [1, 2, 0, 2, 1, 0]; 
function getNum(array) {
    let i = 0;
    array.forEach(element => {
        if (element == 0) {
            i++;
        }
    });
    return i;
}
console.log(getNum(arr));