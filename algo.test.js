const getX = require("./Duncanian");

describe("test for edge cases", () => {
  it("a = 1, b = 5, c = 6 to equal -2", () => {
    expect(getX(1, 5, 6)).toEqual(-2);
  });

  test("check if a/b/c is a string or float value", () => {
    expect(getX("3", 4, 2)).toEqual("Only integers are allowed");
    expect(getX(3.67, 4, 2)).toEqual("Only integers are allowed");
  });

  test("check if a/b/c is empty or a zero", () => {
    expect(getX(0, 4, 2)).toBe("a, b, c should not be empty");
  });
});
