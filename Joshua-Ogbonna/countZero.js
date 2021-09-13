// Create a function that accepts an array parameter

const countZero = (array) => {
  // Initialize a numCount and set it to zero
  let numCount = 0;

  //   Loop through the array
  for (let i = 0; i < array.length; i++) {
    //   Set a conditional, if === 0, increment numCount by 1
    if (array[i] === 0) {
      numCount++;
    }
  }
  //   Return numCount
  return numCount;
};

console.log(countZero([1, 1, 5, 6, 1, 2, 1, 1]));
