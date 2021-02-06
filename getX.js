let getX = (a, b, c) => {
    if (inValidInput(a, b, c)) {
        throw "Invalid input"
    }

    let result = quadratiExp(a, b, c)
    return Math.max(result[0], result[1])
}

let quadratiExp = (a, b, c) => {
    let sqrtItems  = Math.pow(b, 2) - (4 * a * c)

    let numerator = Math.sqrt(
        sqrtItems > 0
        ? sqrtItems
        : Math.abs(sqrtItems)
    )

    let denominator =  2 * a

    let x1 = ((-b + numerator) / denominator).toFixed(2)
    let x2 = ((-b - numerator) / denominator).toFixed(2)

    return [x1, x2]
}

let inValidInput = (a, b, c) => {
    if (isNaN(a) ||isNaN(b) || isNaN(c)) {
        return true
    }
    return false
}

module.exports = getX