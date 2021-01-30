const coefficientsOfRoots = [3, 6, 2];
const getX = (val) => {
   const [a, b, c] = val;
   const inSquareValue = (b * b) - 4 * a * c;
   const d = Math.sqrt(inSquareValue);
   const x1 = (d - b) / (2 * a);
   const x2 = ((d + b) * -1) / (2 * a);
   return x1 > x2 ? x1 : x2
};