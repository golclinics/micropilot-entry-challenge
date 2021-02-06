const getX = require("./getX")

test('test valid ints', () => {
    expect(getX(1, 5, 6)).toBe(-2)
})

test('test signed ints', () => {
    expect(getX(-2, 4, -6)).toBe(2.41)
})

test('test valid float', () => {
    expect(getX(3.0, 4, 2.6)).toBe(-0.02)
})

test('test invalid string', () => {
    expect(() => getX(2, 4, "c")).toThrow()
})