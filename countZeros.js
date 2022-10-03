//A represents the Arr of numbers passed through
function CountZeros(A) {
  //filter the
  const zeroArr = A.filter((item) => {
    return item == 0;
  });
  return zeroArr.length;
}
