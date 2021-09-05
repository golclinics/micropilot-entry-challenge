// a function to count the occurence of zeros(0) in a list

let myList = [1, 4, 9, 0, 6, 2, 8, 0, 6, 4, 0, 3, 7];

let counter = 0;

// function taking in myList and counting number of zeros
const countZeros = (myList) => {
    for (let i = 0; i < myList.length; i++) {
        if (myList[i] === 0) {
            counter += 1;
        }
    }
    return counter;
};

// show the result
console.log(countZeros(myList));