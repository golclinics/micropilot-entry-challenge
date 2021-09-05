let myList = [1, 5, 3, 0, 8, 5, 0, 4, 2, 7, 0];

const countZeros = function(arr, valueToCount) {
    return arr.reduce((counter, valueFromList) => {
        return (valueToCount === valueFromList ? counter + 1 : counter)
    }, 0);
}

console.log(countZeros(myList, 0));