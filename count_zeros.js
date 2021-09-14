const CountZeros = (A) => {
  let zerosCount = 0;
  A.map((elem) => elem === 0 && zerosCount++);

  return zerosCount;
};
