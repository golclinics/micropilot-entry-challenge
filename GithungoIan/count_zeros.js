function CountZeros(elements) {
    let sum = 0;
    elements.forEach((element) => {
        if(element === 0) {
            sum += 1
        }
    })

    return sum;
}

const elements =  [1, 0, 5, 6, 0, 2]
console.log(CountZeros(elements))
