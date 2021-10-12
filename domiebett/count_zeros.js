function CountZeros(A) {
  let zerosCount = 0;
  for (const int of A) {
    if (int === 0) {
      zerosCount++;
    }
  }
  return zerosCount;
}
