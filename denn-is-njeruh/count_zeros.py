def count_zeros(A, n):
  
  flag = 0
  pos = 0
  count = 0
  for c in range(n):
    if A[c] == 0:
      flag = 1
      pos = c
      break

  if flag == 1:
    count = n - pos

  return count



A = [1,2,2,0,0,2,0,6,0,6,7,0,0]
n = len(A)
print("The number of zeros is", count_zeros(A, n))