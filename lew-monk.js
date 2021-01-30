const getX = (a, b, c) => {

    if (a === 0 || undefined) {
        return 'a cant be null'
    } else {
        const square = (b * b) - (4 * a * c)
        const squareRoot = Math.sqrt(square)

        const X1 = (-b + squareRoot) / 2(a)
        const X2 = (-b - squareRoot) / 2(a)

        if (X1 > X2) {
            console.log(`The value of X1 and X2, ${X1} and ${X2} respectively`)
            return X1
        }
        return X2
    }
}