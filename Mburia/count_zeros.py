def count_zeros(A):
  """count_zeros returns the number of times digit 0 individually appears in A.
  'A' could be a zero dimensional array, multidimensional array or a list of numbers """

  # Eg: If A = [24,0,58,0,70] then output will be 2

  string_array = str(A)
  # Strip the array then split it before iterating
  stripped_array = string_array.strip('][').split(', ')
  number_of_zeros  = 0

  for each in stripped_array:
    if each == '0':
      number_of_zeros += 1

  return number_of_zeros


def Count_Zeros(A):
  """ Count_Zeros returns total number of digit 0 in 'A'.
  'A' could be a zero dimensional array, multidimensional array or a list of numbers"""

  # Eg: If A = [309, 24, 0, 560] then output will be 3

  symbols = "[]" # To truncate the array
  list_array = []
  # Append the array to empty list
  list_array.append(A)
  # Map list elements as strings
  initial_list = list(map(str, list_array))

  for element in initial_list:
    clean_list = ""

    for clean in element:
      if clean not in symbols:
        clean_list += clean
        number_of_zeros  = 0

        for each in clean_list:
          if each == '0':
            number_of_zeros += 1

    return number_of_zeros
