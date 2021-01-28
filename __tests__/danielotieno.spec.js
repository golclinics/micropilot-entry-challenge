describe('Get max root function', () => {
  test('it should return the maximum root from the quadratric expression ', () => {
    const a = 1;
    const b = 3;
    const c = -4;

    const output = 1;

    expect(getX(a, b, c)).toEqual(output);
  });
});
