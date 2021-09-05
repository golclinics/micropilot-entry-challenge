let myList = [1, 4, 9, 0, 6, 2, 8, 0, 6, 4, 0, 3, 7];

let counter = 0;

const CountZeros = (myList) => {
    for (let i = 0; i < myList.length; i++) {
        if (myList[i] === 0) {
            counter += 1;
        }
    }
    return counter;
};
console.log(CountZeros(myList));