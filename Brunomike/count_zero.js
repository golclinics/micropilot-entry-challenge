const CountZeros = (numArray) => {
    let count = 0
    numArray.forEach(number => {
        number === 0 ? count++ : count
    })
    return count
}

const myNumbersArray = [1, 0, 5, 6, 0, 2];
let numberOfZeros = CountZeros(myNumbersArray)
console.log(`No of Zeros: ${numberOfZeros}`)