let getX = (a, b, c) => {
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

    let x1 = (-b + numerator) / denominator
    let x2 = (-b - numerator) / denominator

    return [x1, x2]
}

module.exports = getX