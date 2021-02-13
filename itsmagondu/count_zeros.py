def CountZeros(numbers):
  if type(numbers) != list:
    raise TypeError('Invalid data type. Only lists allowed')

  return numbers.count(0)