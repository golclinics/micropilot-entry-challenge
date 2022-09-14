// reducer function counts number of zeros found in array
const reducer = (accumulator, item) => {
  if (item === 0) {
    return accumulator + 1;
  } else {
    return accumulator;
  }
};

// function to check amount of zeros in array passed to it
function countZeros(numArr) {
  let count = 0;
  if (numArr.length > 0) {
    count = numArr.reduce(reducer, 0);
    return count;
  } else {
    // empty array return zero
    return count;
  }
}

module.exports = countZeros;
