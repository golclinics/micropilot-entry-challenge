# Dependency
import numpy as np


# The following function returns the number of times digit 0 individually appears in 'A'
# 'A' could be a zero dimensional array, multidimensional array or a list of numbers
# Eg: If A = [24,0,58,0,70] then output will be 2

def count_zeros(A):
  array = np.asarray(A)
  number_of_zeros = (array==0).sum()
  return number_of_zeros

# This next function returns the total number of digit 0 in 'A'
# 'A' could be a zero dimensional array, multidimensional array or a list of numbers
# Eg: If A = [309, 24, 0, 560] then output will be 3

def countzeros(A):

  empty_list = []

  for each in np.array(A).ravel():
    digits = [int(digit) for digit in str(each)]
    empty_list.extend(digits)
    number_of_zeros = len([0 for number in empty_list if number == 0])
  return number_of_zeros