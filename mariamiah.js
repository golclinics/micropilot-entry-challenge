const getX = (a, b, c) => {
    const discriminant = ((b ** 2) - (4 * a * c))
    if(discriminant > 0) {
        const x1 = ((-1 * b) + Math.sqrt(discriminant)) / (2 * a)
        const x2 = ((-1 * b) - Math.sqrt(discriminant)) / (2 * a)
        return Math.max(x1, x2)
    } else {
        return null
    }
    
}
module.exports = getX;
