const getX  = require('./mariamiah.js');

describe('getX function', () => {
    it('should return max value', () => {
        const a = 4
        const b = 5
        const c = -6
        const result = getX(a, b, c);
        expect(result).toEqual(0.75)
    })

    it('should return null if discriminant is less than 0', () => {
        const a = 4
        const b = 5
        const c = 6
        const result = getX(a, b, c);
        expect(result).toEqual(null)
    })
})